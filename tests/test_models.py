from models import Animal, Vaccination


def test_create_animal(animal: Animal) -> None:
    assert animal.animal_id == 1
    assert animal.name == "Барсик"
    assert animal.species == "кот"
    assert animal.age == 3
    assert animal.owner == "Иванов И.И."
    assert animal.vaccinations == []


def test_animal_str(animal: Animal) -> None:
    text = str(animal)
    assert "Барсик" in text
    assert "кот" in text
    assert "[1]" in text


def test_animal_to_dict(animal: Animal) -> None:
    data = animal.to_dict()
    assert data["id"] == 1
    assert data["name"] == "Барсик"
    assert data["species"] == "кот"
    assert data["age"] == 3
    assert data["owner"] == "Иванов И.И."
    assert "created" in data


def test_animal_from_dict() -> None:
    data = {
        "id": 10,
        "name": "Шарик",
        "species": "собака",
        "age": 4,
        "owner": "Козлов К.К.",
        "created": "2026-01-01",
    }
    animal = Animal.from_dict(data)
    assert animal.animal_id == 10
    assert animal.name == "Шарик"
    assert animal.created == "2026-01-01"


def test_animal_roundtrip(animal: Animal) -> None:
    restored = Animal.from_dict(animal.to_dict())
    assert restored.animal_id == animal.animal_id
    assert restored.name == animal.name
    assert restored.age == animal.age


def test_add_vaccination(animal: Animal,
                         vaccination: Vaccination) -> None:
    """Прививка добавляется в список животного."""
    animal.add_vaccination(vaccination)
    assert len(animal.vaccinations) == 1
    assert animal.vaccinations[0] is vaccination


def test_vaccination_create(vaccination: Vaccination) -> None:
    assert vaccination.animal_id == 1
    assert vaccination.vaccine == "Нобивак"
    assert vaccination.dose == 1.0
    assert vaccination.date == "2026-09-24"


def test_vaccination_str(vaccination: Vaccination) -> None:
    text = str(vaccination)
    assert "Нобивак" in text
    assert "2026-09-24" in text


def test_vaccination_roundtrip(vaccination: Vaccination) -> None:
    restored = Vaccination.from_dict(vaccination.to_dict())
    assert restored.animal_id == vaccination.animal_id
    assert restored.vaccine == vaccination.vaccine
    assert restored.dose == vaccination.dose
    assert restored.date == vaccination.date
