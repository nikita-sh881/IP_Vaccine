"""
import datetime 

def add_animal():
    name = input("Введите кличку животного: ").strip()
    species = input("Введите вид животного: ").strip()
    age = input("Введите возраст животного: ").strip()
    return name, species, age

def add_vaccination(animal_name):
    if animal_name is None:
        print("Сначала добавьте животное.")
        return None
    vaccine = input("Введите название вакцины: ").strip()
    date_in = input("Введите дату или пропустите: ").strip()
    if date_in == "":
        date = datetime.date.today().isoformat()
    else:
        date = date_in
    print(f"Вакцинация '{vaccine}' зафиксирована.")
    return vaccine, date

def find_animal(animal_name):
    if animal_name is None:
        print("В системе нет данных о животных.")
        return False
    query = input("Введите кличку для поиска: ").strip()
    if query.lower() == animal_name.lower():
        print(f"Найдено животное: {animal_name}")
        return True
    else:
        print("Животное не найдено.")
        return False

animal = add_animal()
name, species, age = animal

print(f"Карточка: {name}, {species}, {age} лет")

vaccination = add_vaccination(name)
if vaccination is not None:
    vaccine, date = vaccination
    print(f"Прививка: {vaccine}, дата: {date}")
  
find_animal(name)
"""

from storage import load_data, save_data
from animals import add_animal, find_animal, list_animals
from vaccinations import add_vaccination, show_animal_vaccinations

def show_menu():
    print("\n=== Система учета прививок животных ===")
    print("1. Добавить животное")
    print("2. Показать всех животных")
    print("3. Добавить прививку")
    print("4. Показать прививки животного")
    print("5. Найти животное по кличке")
    print("0. Выход")

def find_animal_menu(data):
    query = input("Введите кличку для поиска: ").strip()
    animal = find_animal(data, query)
    if animal is None:
        print("Животное не найдено.")
        return
    print(f"Найдено: [{animal['id']}] {animal['name']} ({animal['species']}), "
          f"{animal['age']} лет, владелец: {animal['owner']}")

data = load_data()

while True:
    show_menu()
    choice = input("Выберите пункт: ").strip()

    if choice == "1":
        add_animal(data)
    elif choice == "2":
        list_animals(data)
    elif choice == "3":
        add_vaccination(data)
    elif choice == "4":
        show_animal_vaccinations(data)
    elif choice == "5":
        find_animal_menu(data)
    elif choice == "0":
        save_data(data)
        print("Выход.")
        break
    else:
        print("Пункт с таким номером в меню отсутствует.")

