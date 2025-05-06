#!/usr/bin/env python

from load_image import ft_load
import numpy as np
from PIL import Image
import sys


def eprintln(exception: Exception) -> None:
    """Reports and exception to stderr"""
    print(exception, file=sys.stderr)


def error_and_die(exception: Exception) -> None:
    """Reports and exception to stderr and exit with status code '1'"""
    eprintln(exception)
    exit(1)


def ft_invert(a):
    return a - 255


def ft_red(a):
    return a * [1, 0, 0]


def ft_green(a):
    return a * [0, 1, 0]


def ft_blue(a):
    return a == a[..., :1]


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Returns a np.ndarray(uint8t)  to the grey level of an rgb image"""
    return array[..., :] * [0.2989, 0.5870, 0.1140]


def main() -> int:
    try:
        inverted = ft_invert(ft_load("image.jpeg"))
        red = ft_red(ft_load("image.jpeg"))
        Image.fromarray(red).show()
        green = ft_green(ft_load("image.jpeg"))
        Image.fromarray(inverted).show()
        blue = ft_blue(ft_load("image.jpeg"))
        Image.fromarray(blue).show()
        Image.fromarray(green).show()
        grey = ft_grey(ft_load("image.jpeg"))
        Image.fromarray(grey).show()
    except Exception as e:
        error_and_die(e)

    return 0


if __name__ == "__main__":
    main()
