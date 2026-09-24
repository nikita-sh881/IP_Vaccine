import json
import os

from models import Animal, Vaccination


DATA_FILE = os.path.join("data", "animals.json")


def load_data() -> tuple[list[Animal], list[Vaccination]]:
    if not os.path.exists(DATA_FILE):
        return [], []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            raw = json.load(file)
    except json.JSONDecodeError:
        print("Файл данных поврежден. Начинаем с пустого списка.")
        return [], []
    except OSError as error:
        print(f"Ошибка чтения файла: {error}")
        return [], []

    animals: list[Animal] = []
    vaccinations: list[Vaccination] = []

    for item in raw.get("animals", []):
        try:
            animals.append(Animal.from_dict(item))
        except (KeyError, ValueError, TypeError) as error:
            print(f"Пропущена запись животного: {error}")

    for item in raw.get("vaccinations", []):
        try:
            vaccinations.append(Vaccination.from_dict(item))
        except (KeyError, ValueError, TypeError) as error:
            print(f"Пропущена запись прививки: {error}")

    link_vaccinations(animals, vaccinations)
    return animals, vaccinations


def link_vaccinations(animals: list[Animal],
                      vaccinations: list[Vaccination]) -> None:
    index = {animal.animal_id: animal for animal in animals}
    for vaccination in vaccinations:
        animal = index.get(vaccination.animal_id)
        if animal is not None:
            animal.add_vaccination(vaccination)


def save_data(animals: list[Animal],
              vaccinations: list[Vaccination]) -> None:
    payload = {
        "animals": [a.to_dict() for a in animals],
        "vaccinations": [v.to_dict() for v in vaccinations],
    }
    try:
        os.makedirs("data", exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(payload, file, ensure_ascii=False, indent=4)
        print("Данные сохранены.")
    except OSError as error:
        print(f"Ошибка сохранения файла: {error}")
