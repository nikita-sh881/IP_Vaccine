from models import Animal


def add_animal(animals: list[Animal]) -> Animal | None:
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

    new_id = max((a.animal_id for a in animals), default=0) + 1
    animal = Animal(new_id, name, species, age, owner)
    animals.append(animal)
    print(f"Животное '{name}' добавлено (id={new_id}).")
    return animal


def find_animal(animals: list[Animal], query: str) -> Animal | None:
    for animal in animals:
        if animal.name.lower() == query.lower():
            return animal
    return None


def find_animal_by_id(animals: list[Animal],
                      animal_id: int) -> Animal | None:
    for animal in animals:
        if animal.animal_id == animal_id:
            return animal
    return None


def list_animals(animals: list[Animal]) -> None:
    if not animals:
        print("Список животных пуст.")
        return

    print("\n--- Список животных ---")
    for animal in animals:
        print(animal)
        if animal.vaccinations:
            for vaccination in animal.vaccinations:
                print(f"    — {vaccination}")
        else:
            print("    — прививок нет")
