from storage import load_data, save_data
from animals import add_animal, find_animal, list_animals
from vaccinations import add_vaccination, show_animal_vaccinations


def show_menu() -> None:
    print("\n=== Система учета прививок животных ===")
    print("1. Добавить животное")
    print("2. Показать всех животных")
    print("3. Добавить прививку")
    print("4. Показать прививки животного")
    print("5. Найти животное по кличке")
    print("0. Выход")


def find_animal_menu(animals) -> None:
    query = input("Введите кличку для поиска: ").strip()
    animal = find_animal(animals, query)
    if animal is None:
        print("Животное не найдено.")
    else:
        print(f"Найдено: {animal}")


def main() -> None:
    animals, vaccinations = load_data()

    while True:
        show_menu()
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            add_animal(animals)
        elif choice == "2":
            list_animals(animals)
        elif choice == "3":
            add_vaccination(animals, vaccinations)
        elif choice == "4":
            show_animal_vaccinations(animals)
        elif choice == "5":
            find_animal_menu(animals)
        elif choice == "0":
            save_data(animals, vaccinations)
            print("Выход.")
            break
        else:
            print("Пункт с таким номером в меню отсутствует.")


if __name__ == "__main__":
    main()
