#!/usr/bin/env python

import sys as sys
from typing import List, Optional, NoReturn


def parse_arguments(words: str, max_len_str: str) -> Optional[tuple]:
    # parse arguments and checks that the second one is numeric
    if not max_len_str.isnumeric():
        return None
    return (words, int(max_len_str))


def error_and_die() -> NoReturn:
    # closes the program with error message
    print("AssertionError: the arguments are bad", file=sys.stderr)
    sys.exit(1)


def process_arguments(words: str, min_len: int) -> List[str]:
    # process the arguments by splitting and filtering words by min len
    return list(filter(lambda w: len(w) > min_len, words.split()))


def main() -> None:
    # program entry point
    if len(sys.argv) != 3:
        error_and_die()

    maybe_args: Optional[tuple] = parse_arguments(*sys.argv[1:])
    if maybe_args is not None:
        print(process_arguments(*maybe_args))
    else:
        error_and_die()
    return


if __name__ == "__main__":
    main()
