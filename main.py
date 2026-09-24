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
