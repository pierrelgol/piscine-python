#!/usr/bin/env python3

import sys


def eprintln(exception: Exception) -> None:
    """Reports an error to stderr"""
    print(exception, file=sys.stderr)


def errorAndDie(exception: Exception) -> None:
    """Reports an error to stderr and exits"""
    eprintln(exception)
    sys.exit(1)


def getUserInput() -> str:
    """Returns input string from sys.argv or prompt"""
    if len(sys.argv) == 1:
        try:
            return input("What is the text to count? ") + "\n"
        except (EOFError, KeyboardInterrupt):
            return ""
    else:
        return sys.argv[1]


def countText(text: str) -> dict[str, int]:
    """Counts various character types in the input text"""
    count = {
        "lower": 0,
        "upper": 0,
        "space": 0,
        "punct": 0,
        "value": 0,
        "digit": 0,
    }

    for char in text:
        if char.islower():
            count["lower"] += 1
        elif char.isupper():
            count["upper"] += 1
        elif char.isspace():
            count["space"] += 1
        elif char in r"!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~\"":
            count["punct"] += 1
        elif char.isdigit():
            count["digit"] += 1
        count["value"] += 1
    return count


def printResult(results: dict[str, int]) -> None:
    """Displays the character counts"""
    print("The text contains")
    print(f"{results['value']} characters:")
    print(f"{results['upper']} upper-case letters")
    print(f"{results['lower']} lower-case letters")
    print(f"{results['punct']} punctuation marks")
    print(f"{results['space']} spaces")
    print(f"{results['digit']} digits")


def main() -> int:
    """program entry point"""
    try:
        msg = "AssertionError: more than one argument is provided"
        if len(sys.argv) > 2:
            raise AssertionError(msg)
        text = getUserInput()
        results = countText(text)
        printResult(results)
    except Exception as e:
        errorAndDie(e)
    return 0


if __name__ == "__main__":
    main()
