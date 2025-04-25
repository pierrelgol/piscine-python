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


def ft_invert(array: np.ndarray) -> np.ndarray:
    return np.clip(255 - array[:, :, 0:3], 0, 255).astype(np.uint8)


def ft_red(array: np.ndarray) -> np.ndarray:
    red = np.zeros_like(array)
    red[:, :, 0] = array[:, :, 0]
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    green = np.zeros_like(array)
    green[:, :, 1] = array[:, :, 1]
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    blue = np.zeros_like(array)
    blue[:, :, 2] = array[:, :, 2]
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Returns a np.ndarray(uint8t) corresponding to the grey level of an rgb image"""
    return np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])


def main() -> int:
    try:
        # inverted = ft_invert(ft_load("image.jpeg"))
        # red = ft_red(ft_load("image.jpeg"))
        # green = ft_green(ft_load("image.jpeg"))
        blue = ft_blue(ft_load("image.jpeg"))
        # grey = ft_grey(ft_load("image.jpeg"))
        # Image.fromarray(inverted).show()
        # Image.fromarray(red).show()
        # Image.fromarray(green).show()
        Image.fromarray(blue).show()
        # Image.fromarray(grey).show()
    except Exception as e:
        error_and_die(e)

    return 0


if __name__ == "__main__":
    main()
