#!/usr/bin/env python

import sys
from typing import Dict, List, NoReturn


def getMorseMap() -> Dict[str, str]:
    # provides the Morse map
    # fmt: off
    morse_map: Dict[str, str] = {
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


def error_and_die() -> NoReturn:
    # function that terminates in case of erros
    print("AssertionError: the arguments are bad")
    sys.exit(1)


def fromStringToMorseCode(input: str) -> str:
    # conversion function
    to_morse = getMorseMap()
    morsed: List[str] = []
    for char in input:
        upper_char = char.upper()
        if upper_char not in to_morse:
            error_and_die()
        morsed.append(to_morse[upper_char])
    return " ".join(morsed)


def main() -> None:
    if len(sys.argv) != 2:
        error_and_die()
    print(fromStringToMorseCode(sys.argv[1]))

    return


if __name__ == "__main__":
    main()
