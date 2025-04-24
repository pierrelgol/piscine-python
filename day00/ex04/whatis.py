#!/usr/bin/env python

import sys as sys


def isEven(number: int) -> bool:
    """Returns 'True' if number is even"""
    return abs(number) & 1 == 0


def intFromString(number: str) -> int | None:
    """
    Returns an 'int' if 'number' conversion is safe or 'None' if converting
    'number' would raise an exception
    """
    if number.isnumeric():
        return int(number)
    else:
        return None


def eprintln(exception: AssertionError) -> None:
    """Print an 'AssertionError' to stderr."""
    print(exception, file=sys.stderr)


def errorAndDie(exception: AssertionError) -> None:
    """Print an 'AssertionError' to stderr. And exit with status code '1'"""
    eprintln(exception)
    sys.exit(1)


def printResult(is_even: bool) -> None:
    """Prints I'm Even if is even else I'm Odd."""
    if is_even:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main() -> int:
    """The program entry point. If that wasn't fucking obvious."""
    if len(sys.argv) == 1:
        return 0

    try:
        if len(sys.argv) > 2:
            raise AssertionError("AssertionError: more than one argument is provided")
    except AssertionError as ae:
        errorAndDie(ae)

    try:
        number: int | None = intFromString(number=sys.argv[1])
        if number is None:
            raise AssertionError("AssertionError: argument is not an integer")
        else:
            printResult(is_even=isEven(number=number))
    except AssertionError as ae:
        errorAndDie(ae)
    return 0


if __name__ == "__main__":
    main()
