#!/usr/bin/env python3
import sys as sys


def countText(input) -> None:
    # This function counts each characters by kind

    total_lower: int = 0
    total_upper: int = 0
    total_space: int = 0
    total_punct: int = 0
    total_value: int = 0
    total_digit: int = 0

    for char in input:
        if char.islower():
            total_lower += 1
        elif char.isupper():
            total_upper += 1
        elif char.isspace():
            total_space += 1
        elif char in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
            total_punct += 1
        elif char.isdigit():
            total_digit += 1
        total_value += 1

    print(f"The text contains {total_value} characters:")
    print(f"{total_upper} letters")
    print(f"{total_lower} letters")
    print(f"{total_punct} punctuation marks")
    print(f"{total_space} spaces")
    print(f"{total_digit} digits")


def promptUser() -> None:
    # This function prompts the user for inputs.
    print("What is the text to count?")
    input_str: str = ""
    try:
        input_str = input()
        input_str += "\n"
    except EOFError:
        return countText(input_str)
    except KeyboardInterrupt:
        return countText(input_str + " ")
    return countText(input_str)


def main() -> int:
    # Program entry point
    if len(sys.argv) == 1:
        promptUser()
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
    else:
        countText(sys.argv[1])
    return 0


if __name__ == "__main__":
    main()
