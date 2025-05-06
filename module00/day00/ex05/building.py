#!/usr/bin/env python3
import sys as sys


def eprintln(exception: AssertionError) -> None:
    """Reports an AssertionError to 'stderr'"""
    print(exception, file=sys.stderr)


def errorAndDie(exception: AssertionError) -> None:
    """Reports an AssertionError to 'stderr' and exit with status code 1"""
    eprintln(exception=exception)
    sys.exit(1)


def getUserInput() -> str:
    """Returns a string of user inputs from sys.argv[1] or from 'input()'"""
    if len(sys.argv) == 1:
        input_str: str = ""
        try:
            input_str = input("What is the text to count?")
            input_str += "\n"
        except EOFError:
            return input_str
        except KeyboardInterrupt:
            return input_str + " "
        return input_str
    else:
        return sys.argv[1]


def countText(input: str) -> dict[str:int]:
    """
    Returns a dict[str:int] that contains a distinct count of letters in input
    by the following kind:
        - "lower",
        - "upper",
        - "space",
        - "punct",
        - "value",
        - "digit",
    """
    count: dict[str:int] = {
        "lower": 0,
        "upper": 0,
        "space": 0,
        "punct": 0,
        "value": 0,
        "digit": 0,
    }

    for char in input:
        if char.islower():
            count["lower"] += 1
        elif char.isupper():
            count["upper "] += 1
        elif char.isspace():
            count["space"] += 1
        elif char in "!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" + '"':
            count["punct"] += 1
        elif char.isdigit():
            count["digit"] += 1
        count["value"] += 1
    return count


def printResult(results: dict[str:int]) -> None:
    """
    This function display the keys of results and their values
    """
    print("The text contains")
    print(f"{results['value']} characters:")
    print(f"{results['upper']} letters")
    print(f"{results['lower']} letters")
    print(f"{results['punct']} punctuation marks")
    print(f"{results['space']} spaces")
    print(f"{results['digit']} digits")


def main() -> int:
    """program entry point"""
    try:
        msg = "AssertionError: more than one argument is provided"
        if len(sys.argv) > 2:
            raise AssertionError(msg)
        else:
            printResult(countText(getUserInput()))
    except AssertionError as ae:
        errorAndDie(ae)
    except Exception as e:
        errorAndDie(e)
    return 0


if __name__ == "__main__":
    main()
