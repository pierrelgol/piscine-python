#!/usr/bin/env python

from typing import Callable


def square(x: int | float) -> int | float:
    """This function returns the square of a a natural number 'x'"""
    if not x or not isinstance(x, int | float):
        raise TypeError("Invalid type for x")
    return x * x


def pow(x: int | float) -> int | float:
    """This function returns the power of a a natural number 'x'"""
    if not x or not isinstance(x, int | float):
        raise TypeError("Invalid type for x")

    return x**x


def outer(x: int | float, function: Callable) -> Callable:
    """
    Returns a callable object that applies `function` to the previous result on each call.
    """
    current = x

    def inner() -> float:
        nonlocal current
        current = function(current)
        return current

    return inner


def main() -> None:
    """Entry point"""
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())
    return


if __name__ == "__main__":
    main()
