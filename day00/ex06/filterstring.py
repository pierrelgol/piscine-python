#!/usr/bin/env python

import sys


def parse_arguments(words: str, max_len_str: str) -> tuple | None:
    """Returns a tuple of '(str, int)' or None if max_len_str is not numeric"""
    if not max_len_str.isnumeric():
        return None
    return (words, int(max_len_str))


def eprintln(exception: any) -> None:
    """Reports an AssertionError to stderr"""
    print(exception, file=sys.stderr)


def error_and_die(exception: AssertionError) -> None:
    """Reports an AssertionError to stderr and exits with status code '1'"""
    eprintln(exception=exception)
    sys.exit(1)


def process_arguments(words: str, min_len: int) -> list[str]:
    """Returns a list of 'word' whose length is greater than 'min_len'"""
    return list(filter(lambda w="": len(w) > min_len, words.split()))


def main() -> int:
    """Program entry point"""

    try:
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")

        maybe_args = parse_arguments(*sys.argv[1:])

        if maybe_args is None:
            raise AssertionError("AssertionError: the arguments are bad")
        else:
            print(process_arguments(*maybe_args))
    except AssertionError as ae:
        error_and_die(ae)
    except Exception as e:
        error_and_die(e)

    return 0


if __name__ == "__main__":
    main()
