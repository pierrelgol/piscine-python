#!/usr/bin/env python


class calculator:
    """
    A calculator that supports basic operations on a list of floats and a scalar.
    """

    def __init__(self, object):
        """
        Initializes the calculator with a list of float values.
        """
        self.objects = object

    def __add__(self, object):
        """
        Adds a scalar to each element of the vector.
        """
        self.objects = [x + object for x in self.objects]
        print(self.objects)

    def __sub__(self, object):
        """
        Subtracts a scalar from each element of the vector.
        """
        self.objects = [x - object for x in self.objects]
        print(self.objects)

    def __mul__(self, object):
        """
        Multiplies each element of the vector by a scalar.
        """
        self.objects = [x * object for x in self.objects]
        print(self.objects)

    def __truediv__(self, object):
        """
        Divides each element of the vector by a scalar.
        """
        if object == 0:
            print("Error: Division by zero.")
        else:
            self.objects = [x / object for x in self.objects]
        print(self.objects)


def main() -> None:
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    return


if __name__ == "__main__":
    main()
