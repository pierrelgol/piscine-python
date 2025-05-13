#!/usr/bin/env python

from load_image import ft_load
import numpy as np
import sys
import math as m
from PIL import Image


def eprintln(exception: Exception) -> None:
    """Reports and exception to stderr"""
    print(exception, file=sys.stderr)


def error_and_die(exception: Exception) -> None:
    """Reports and exception to stderr and exit with status code '1'"""
    eprintln(exception)
    exit(1)


def rotate_image(image: np.ndarray, amount_deg: float) -> np.ndarray:
    """
    This function takes an image as an 'ndarray'
    and an angle, and rotates the image
    """
    amount_rad: float = m.radians(amount_deg)
    cos_theta: float = m.cos(amount_rad)
    sin_theta = m.sin(amount_rad)
    height, width = image.shape[:2]
    center_y: float = height / 2.0
    center_x: float = width / 2.0
    rotated = np.zeros_like(image)

    for y_prime in range(height):
        for x_prime in range(width):
            x_shift: float = x_prime - center_x
            y_shift: float = y_prime - center_y

            x_rotated: float = cos_theta * x_shift + sin_theta * y_shift
            y_rotated: float = -sin_theta * x_shift + cos_theta * y_shift

            x_centered: float = x_rotated + center_x
            y_centered: float = y_rotated + center_y

            x_trunc: int = int(round(x_centered))
            y_trunc: int = int(round(y_centered))

            if 0 <= x_trunc < width and 0 <= y_trunc < height:
                rotated[y_prime, x_prime, :3] = image[y_trunc, x_trunc, :3]

    return rotated


def main() -> int:
    """Program entry point"""
    image: np.ndarray

    try:
        image = ft_load("image.jpeg")
        image = rotate_image(image, 90)
    except Exception as e:
        error_and_die(e)

    Image.fromarray(image).show()
    return 0


if __name__ == "__main__":
    main()
