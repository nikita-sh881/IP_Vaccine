import datetime

from models import Animal, Vaccination
from animals import find_animal_by_id

def add_vaccination(animals: list[Animal],
                    vaccinations: list[Vaccination]) -> bool:
    if not animals:
        print("Сначала добавьте хотя бы одно животное.")
        return False

    id_input = input("Введите id животного: ").strip()
    try:
        animal_id = int(id_input)
    except ValueError:
        print("id должен быть числом.")
        return False

    animal = find_animal_by_id(animals, animal_id)
    if animal is None:
        print("Животное с таким id не найдено.")
        return False

    vaccine = input("Введите название вакцины: ").strip()
    if vaccine == "":
        print("Ошибка: название вакцины обязательно.")
        return False

    dose_input = input("Введите дозировку (мл): ").strip()
    try:
        dose = float(dose_input)
        if dose <= 0:
            raise ValueError
    except ValueError:
        print("Дозировка указана некорректно, установлено 0.0.")
        dose = 0.0

    date_input = input("Введите дату (ГГГГ-ММ-ДД) или Enter: ").strip()
    date = date_input or datetime.date.today().isoformat()

    vaccination = Vaccination(animal_id, vaccine, dose, date)
    vaccinations.append(vaccination)
    animal.add_vaccination(vaccination)
    print(f"Вакцинация '{vaccine}' для '{animal.name}' зафиксирована.")
    return True


def find_vaccinations_by_animal(
        animal: Animal) -> list[Vaccination]:
    return list(animal.vaccinations)


def show_animal_vaccinations(animals: list[Animal]) -> None:
    if not animals:
        print("Список животных пуст.")
        return

    id_input = input("Введите id животного: ").strip()
    try:
        animal_id = int(id_input)
    except ValueError:
        print("id должен быть числом.")
        return

    animal = find_animal_by_id(animals, animal_id)
    if animal is None:
        print("Животное с таким id не найдено.")
        return

    print(f"\n--- Прививки животного '{animal.name}' ---")
    if not animal.vaccinations:
        print("Прививок нет.")
        return
    for vaccination in animal.vaccinations:
        print(vaccination)
