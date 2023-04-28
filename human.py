import typing

class Human:
    def __init__(self,
        first_name: str,
        last_name: str,
        birthday: str,
        age: int,
        health: int,
        major: str
    ) -> None:
        self.name = f"{first_name.capitalize()} {last_name.capitalize()}"
        self.birthday = birthday
        self.age = age
        self.health = health
        self.major = major.capitalize()

    def print_name(self) -> None:
        print(self.name)


    def check_old_enough_to_drink(self) -> bool:
        return True if self.age >= 21 else False


    def attack_human(self, other_person):
        other_person.health -= 25
        
        print(f"{self.name} attacked {other_person.name} and they are badly hurt!")
        print(other_person.health)
