import json
import os


DATA_FILE = os.path.join("data", "animals.json")

def load_data():
    """Загружает данные из JSON-файла. Если файла нет — возвращает пустую структуру."""
    if not os.path.exists(DATA_FILE):
        return {"animals": [], "vaccinations": []}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Файл данных поврежден. Начинаем с пустого списка.")
        return {"animals": [], "vaccinations": []}
    except OSError as error:
        print(f"Ошибка чтения файла: {error}")
        return {"animals": [], "vaccinations": []}

    if "animals" not in data:
        data["animals"] = []
    if "vaccinations" not in data:
        data["vaccinations"] = []
    return data

def save_data(data):
    try:
        os.makedirs("data", exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Данные сохранены.")
    except OSError as error:
        print(f"Ошибка сохранения файла: {error}")
