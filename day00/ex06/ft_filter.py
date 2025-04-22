#!/usr/bin/env python3

from typing import Callable, Iterable, Iterator, TypeVar, Any

T = TypeVar("T")


def ft_filter(fn: Callable[[T], Any], it: Iterable[T]) -> Iterator[T]:
    return iter([elem for elem in it if fn(elem)])


def isOdd(item: int) -> bool:
    return item & 1 == 1


def main() -> None:
    # Program Entry point
    items = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    items = filter(isOdd, items)
    for item in items:
        print(item, end="")

    print()

    items = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    items = ft_filter(isOdd, items)
    for item in items:
        print(item, end="")
    return


if __name__ == "__main__":
    main()
