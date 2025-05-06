#!/usr/bin/env python

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Represents a king who inherits from both Baratheon and Lannister families.
    """

    def __init__(self, first_name, is_alive=True):
        """
        Initializes the king with name, life status and default Baratheon features.
        """
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """Returns eye color."""
        return self.eyes

    def set_eyes(self, color):
        """Sets eye color."""
        self.eyes = color

    def get_hairs(self):
        """Returns hair color."""
        return self.hairs

    def set_hairs(self, color):
        """Sets hair color."""
        self.hairs = color


def main() -> None:
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)
    return


if __name__ == "__main__":
    main()
