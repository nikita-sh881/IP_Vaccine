import datetime

def add_animal(data):
    name = input("Введите кличку животного: ").strip()
    species = input("Введите вид животного: ").strip()
    owner = input("Введите ФИО владельца: ").strip()

    if name == "" or species == "":
        print("Ошибка: кличка и вид обязательны.")
        return None

    age_input = input("Введите возраст (лет): ").strip()
    try:
        age = int(age_input)
        if age < 0:
            raise ValueError
    except ValueError:
        print("Возраст указан некорректно, установлено значение 0.")
        age = 0

    new_id = 1
    for animal in data["animals"]:
        if animal["id"] >= new_id:
            new_id = animal["id"] + 1

    animal = {
        "id": new_id,
        "name": name,
        "species": species,
        "age": age,
        "owner": owner,
        "created": datetime.date.today().isoformat(),
    }
    data["animals"].append(animal)
    print(f"Животное '{name}' добавлено (id={new_id}).")
    return new_id


def find_animal(data, query):
    for animal in data["animals"]:
        if animal["name"].lower() == query.lower():
            return animal
    return None

def find_animal_by_id(data, animal_id):
    for animal in data["animals"]:
        if animal["id"] == animal_id:
            return animal
    return None

def list_animals(data):
    if not data["animals"]:
        print("Список животных пуст.")
        return

    print("\n--- Список животных ---")
    for animal in data["animals"]:
        print(f"[{animal['id']}] {animal['name']} ({animal['species']}), "
              f"{animal['age']} лет, владелец: {animal['owner']}")

        animal_vaccinations = [
            v for v in data["vaccinations"] if v["animal_id"] == animal["id"]
        ]
        if animal_vaccinations:
            for v in animal_vaccinations:
                print(f"    — {v['vaccine']}, {v['dose']} мл, {v['date']}")
        else:
            print("    — прививок нет")
