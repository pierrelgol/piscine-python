#!/usr/bin/env python

from abc import ABC, abstractmethod


class Character(ABC):
    """Character Abstract class"""

    @abstractmethod
    def __init__(self, first_name: str = "", is_alive: bool = True):
        """Initialize the character with a name and life status."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Kills the character by setting 'is_alive' to False."""
        pass


class Stark(Character):
    """Concrete Character child class"""

    def __init__(self, first_name: str = "", is_alive: bool = True):
        """Initializes a Stark with a name and life status."""
        super().__init__(first_name=first_name, is_alive=is_alive)

    def die(self):
        """Sets the is_alive attribute to False."""
        self.is_alive = False


def main() -> None:
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    # hodor = Character("hodor")
    # _ = hodor
    return


if __name__ == "__main__":
    main()
