import datetime
from animals import find_animal_by_id

def add_vaccination(data):
    if not data["animals"]:
        print("Сначала добавьте хотя бы одно животное.")
        return False

    id_input = input("Введите id животного: ").strip()
    try:
        animal_id = int(id_input)
    except ValueError:
        print("id должен быть числом.")
        return False

    animal = find_animal_by_id(data, animal_id)
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
    if date_input == "":
        date = datetime.date.today().isoformat()
    else:
        date = date_input

    vaccination = {
        "animal_id": animal_id,
        "vaccine": vaccine,
        "dose": dose,
        "date": date,
    }
    data["vaccinations"].append(vaccination)
    print(f"Вакцинация '{vaccine}' для '{animal['name']}' зафиксирована.")
    return True

def find_vaccinations_by_animal(data, animal_id):
    result = []
    for v in data["vaccinations"]:
        if v["animal_id"] == animal_id:
            result.append(v)
    return result

def show_animal_vaccinations(data):
    if not data["animals"]:
        print("Список животных пуст.")
        return

    id_input = input("Введите id животного: ").strip()
    try:
        animal_id = int(id_input)
    except ValueError:
        print("id должен быть числом.")
        return

    animal = find_animal_by_id(data, animal_id)
    if animal is None:
        print("Животное с таким id не найдено.")
        return

    vaccinations = find_vaccinations_by_animal(data, animal_id)
    print(f"\n--- Прививки животного '{animal['name']}' ---")
    if not vaccinations:
        print("Прививок нет.")
        return
    for v in vaccinations:
        print(f"{v['date']}: {v['vaccine']}, {v['dose']} мл")
