#!/usr/bin/env python

import numpy as np
import sys
from load_image import ft_load
from PIL import Image


def eprintln(exception: Exception) -> None:
    """Reports and exception to stderr"""
    print(exception, file=sys.stderr)


def error_and_die(exception: Exception) -> None:
    """Reports and exception to stderr and exit with status code '1'"""
    eprintln(exception)
    exit(1)


def clamp(cmin: int, cmax: int, value: int) -> int:
    """Clamp a 'value' to the interval [min, max]"""
    return max(min(value, cmax), cmin)


def zoom_centered(image: np.ndarray, zoom_percent: float) -> np.ndarray:
    """Returns a centered slice of image based on a percentage from [0, 1]"""
    height, width = image.shape[:2]
    new_height = int(height * clamp(0, 1, zoom_percent))
    new_width = int(width * clamp(0, 1, zoom_percent))
    center_x = width // 2
    center_y = height // 2
    y1 = int(center_y - new_height)
    y2 = int(center_y + new_height)
    x1 = int(center_x - new_width)
    x2 = int(center_x + new_width)
    return image[y1:y2, x1:x2:]


def zoom_slice(image: np.ndarray, nheight: int, nwidth: int) -> np.ndarray:
    """Returns a centered slice of image based on a desired height/width"""
    height, width = image.shape[:2]
    center_x = int(width // 2)
    center_y = int(height // 2)
    half_h = int(nheight // 2)
    half_w = int(nwidth // 2)

    y1 = max(center_y - half_h, 0)
    y2 = min(center_y + half_h, height)
    x1 = max(center_x - half_w, 0)
    x2 = min(center_x + half_w, width)

    return image[y1:y2, x1:x2, :]


def from_rgb_to_grey(img: np.ndarray) -> np.ndarray:
    """
    Returns a np.ndarray(uint8t) corresponding
    to the grey level of an rgb image
    """
    g = 0.2989 * img[:, :, 0] + 0.5870 * img[:, :, 1] + 0.1140 * img[:, :, 2]
    g = np.clip(g, 0, 255)
    g = g.astype(np.uint8)
    return g


def load_image_and_zoom_centered() -> None:
    """Try to load an image, zoom center, grey and show"""
    try:
        image = ft_load("image.jpeg")
        print(f"The shape of the image is: {image.shape}")
        image_zoomed = zoom_centered(image, 0.25)
        grey = from_rgb_to_grey(image_zoomed)
        Image.fromarray(grey).show()
        print(f"New shape after slicing: {grey.shape} or {grey.shape[:2]}")
    except Exception as e:
        error_and_die(e)


def load_image_and_zoom_sliced() -> None:
    """Try to load an image, zoom sliced, grey and show"""
    try:
        image = ft_load("image.jpeg")
        print(f"The shape of the image is: {image.shape}")
        image_zoomed = zoom_slice(image, 400, 400)
        grey = from_rgb_to_grey(image_zoomed)
        Image.fromarray(grey).show()
        print(f"New shape after slicing: {grey.shape} or {grey.shape[:2]}")
    except Exception as e:
        error_and_die(e)


def main() -> int:
    """Program entry point"""
    load_image_and_zoom_centered()
    load_image_and_zoom_sliced()
    return 0


if __name__ == "__main__":
    main()
