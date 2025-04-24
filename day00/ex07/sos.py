#!/usr/bin/env python

import sys


def getMorseMap() -> dict[str, str]:
    """Returns a map of morse code mapping"""
    # fmt: off
    morse_map: dict[str, str] = {
        'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
        'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
        'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
        'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
        'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
        '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
        '8': '---..',  '9': '----.',
        ' ': '/',
    }
    # fmt: on
    return morse_map


def eprintln(exception: any) -> None:
    """Reports an AssertionError to stderr"""
    print(exception, file=sys.stderr)


def error_and_die(exception: AssertionError) -> None:
    """Reports an AssertionError to stderr and exits with status code '1'"""
    eprintln(exception=exception)
    sys.exit(1)


def fromStringToMorseCode(input: str) -> str:
    """Returns a string converting any alphanumeric into morse code"""
    to_morse = getMorseMap()
    morsed: list[str] = []
    for char in input:
        upper_char = char.upper()
        try:
            if upper_char not in to_morse:
                raise AssertionError("AssertionError: the arguments are bad")
            else:
                morsed.append(to_morse[upper_char])
        except AssertionError as ae:
            error_and_die(ae)
        except Exception as e:
            error_and_die(e)
    return " ".join(morsed)


def main() -> None:
    """Program entry point"""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: the arguments are bad")
    except AssertionError as ae:
        error_and_die(ae)
    except Exception as e:
        error_and_die(e)

    print(fromStringToMorseCode(sys.argv[1]))

    return


if __name__ == "__main__":
    main()
