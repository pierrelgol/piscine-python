#!/usr/bin/env python


class calculator:
    """
    A calculator that supports vector operations via decorated class methods.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Computes and prints the dot product of two vectors.
        """
        print("Dot product is:", sum(a * b for a, b in zip(V1, V2)))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Computes and prints the element-wise sum of two vectors.
        """
        print("Add Vector is :", [float(e) for e in [a + b for a, (b) in zip(V1, V2)]])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Computes and prints the element-wise difference of two vectors.
        """
        print("Sous Vector is:", [float(e) for e in [a - b for a, (b) in zip(V1, V2)]])


def main() -> None:
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)
    return


if __name__ == "__main__":
    main()
