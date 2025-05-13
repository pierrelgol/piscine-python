#!/usr/bin/env python

import sys


def parse_arguments(words: str, max_len_str: str) -> tuple | None:
    """Returns a tuple of '(str, int)' or None if max_len_str is not numeric"""
    if not max_len_str.isnumeric():
        return None
    return (words, int(max_len_str))


def error_and_die(exception: any) -> None:
    """Reports an AssertionError to stderr and exits with status code '1'"""
    print(exception, file=sys.stderr)
    sys.exit(1)


def process_arguments(words: str, min_len: int) -> list[str]:
    """Returns a list of 'word' whose length is greater than 'min_len'"""
    return list(filter(lambda w="": len(w) > min_len, words.split()))


def main() -> int:
    """Program entry point"""

    sys.tracebacklimit = 0

    assert len(sys.argv) == 3, "the arguments are bad"
    maybe_args = parse_arguments(*sys.argv[1:])

    assert maybe_args is not None, "the arguments are bad"
    print(process_arguments(*maybe_args))


if __name__ == "__main__":
    main()
