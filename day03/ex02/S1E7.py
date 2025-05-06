#!/usr/bin/env python

from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str = "", is_alive: bool = True):
        """Initializes a Baratheon with a name and life status."""
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Sets the is_alive attribute to False."""
        self.is_alive = False

    def __str__(self) -> str:
        """formatting function for 'self'"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """String representation of 'self'"""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str = "", is_alive: bool = True):
        """Initializes a Lannister with a name and life status."""
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Sets the is_alive attribute to False."""
        self.is_alive = False

    def __str__(self) -> str:
        """formatting function for 'self'"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """String representation of 'self'"""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Class method to create a Lannister character.
        """
        return cls(first_name, is_alive)


def main() -> None:
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")
    return


if __name__ == "__main__":
    main()
