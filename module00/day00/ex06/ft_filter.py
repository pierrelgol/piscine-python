#!/usr/bin/env python3


def ft_filter(fn, it):
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None,
    return the items that are true.
    """
    if fn is None:
        return (item for item in it if item)
    else:
        return (item for item in it if fn(item))


def main():
    """Program entry point"""
    print(list(ft_filter(lambda x: x > 5, (1, 2, 3, 4, 5, 6, 7, 8, 9))))
    print(list(filter(lambda x: x > 5, (1, 2, 3, 4, 5, 6, 7, 8, 9))))
    print(filter.__doc__)
    print(ft_filter.__doc__)
    return


if __name__ == "__main__":
    main()
