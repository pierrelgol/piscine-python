#!/usr/bin/env python

from typing import Any


def callLimit(limit: int):
    """
    A decorator factory that limits the number of calls to a function.

    Args:
        limit (int): Maximum number of allowed calls.

    Returns:
        Callable: A decorator that enforces the call limit.
    """
    count = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter


@callLimit(3)
def f():
    """For testing"""
    print("f()")


@callLimit(1)
def g():
    """For testing"""
    print("g()")


def main() -> None:
    """Entry point"""
    for _ in range(3):
        f()
        g()
    return


if __name__ == "__main__":
    main()
