#!/usr/bin/env python

from dataclasses import dataclass, field
import random
import string


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Method to initialize the login/id"""
        self.login = f"{self.name[0].upper()}{self.surname.lower()}"
        self.id = generate_id()


def main() -> None:
    student = Student(name="Edward", surname="agle")
    print(student)

    # student = Student(name="Edward", surname="agle", id="toto")
    # print(student)
    return


if __name__ == "__main__":
    main()
