import datetime

class Animal:
    def __init__(self, animal_id: int, name: str, species: str,
                 age: int, owner: str,
                 created: str | None = None) -> None:
        self.animal_id = animal_id
        self.name = name
        self.species = species
        self.age = age
        self.owner = owner
        self.created = created or datetime.date.today().isoformat()
        self.vaccinations: list["Vaccination"] = []

    def add_vaccination(self, vaccination: "Vaccination") -> None:
        """Привязывает прививку к этому животному."""
        self.vaccinations.append(vaccination)

    def to_dict(self) -> dict:
        return {
            "id": self.animal_id,
            "name": self.name,
            "species": self.species,
            "age": self.age,
            "owner": self.owner,
            "created": self.created,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Animal":
        return cls(
            animal_id=int(data["id"]),
            name=str(data["name"]),
            species=str(data["species"]),
            age=int(data["age"]),
            owner=str(data["owner"]),
            created=data.get("created"),
        )

    def __str__(self) -> str:
        return (f"[{self.animal_id}] {self.name} ({self.species}), "
                f"{self.age} лет, владелец: {self.owner}")


class Vaccination:
    def __init__(self, animal_id: int, vaccine: str,
                 dose: float, date: str) -> None:
        self.animal_id = animal_id
        self.vaccine = vaccine
        self.dose = dose
        self.date = date

    def to_dict(self) -> dict:
        return {
            "animal_id": self.animal_id,
            "vaccine": self.vaccine,
            "dose": self.dose,
            "date": self.date,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Vaccination":
        return cls(
            animal_id=int(data["animal_id"]),
            vaccine=str(data["vaccine"]),
            dose=float(data["dose"]),
            date=str(data["date"]),
        )

    def __str__(self) -> str:
        return f"{self.date}: {self.vaccine}, {self.dose} мл"
