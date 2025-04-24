#!/usr/bin/env python3


def ft_filter(fn, it):
    """Works just like the filter builtins"""
    if fn is None:
        return (item for item in it if item)
    else:
        return (item for item in it if fn(item))


def main():
    """Program entry point"""
    print(list(ft_filter(lambda x: x > 5, (1, 2, 3, 4, 5, 6, 7, 8, 9))))
    print(list(filter(lambda x: x > 5, (1, 2, 3, 4, 5, 6, 7, 8, 9))))
    return


if __name__ == "__main__":
    main()
