#!/usr/bin/env python

import numpy as np
import sys
from load_image import ft_load
from PIL import Image


def eprintln(exception: Exception) -> None:
    print(exception, file=sys.stderr)


def error_and_die(exception: Exception) -> None:
    eprintln(exception)
    exit(1)


def clamp(cmin: int, cmax: int, value: int) -> int:
    return max(min(value, cmax), cmin)


def zoom_centered(image: np.ndarray, zoom_percent: float) -> np.ndarray:
    if zoom_percent == 0.0:
        return image
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


def zoom_slice(image: np.ndarray, new_height: int, new_width: int) -> np.ndarray:
    height, width = image.shape[:2]
    center_x = int(width // 2)
    center_y = int(height // 2)
    half_h = int(new_height // 2)
    half_w = int(new_width // 2)

    y1 = max(center_y - half_h, 0)
    y2 = min(center_y + half_h, height)
    x1 = max(center_x - half_w, 0)
    x2 = min(center_x + half_w, width)

    return image[y1:y2, x1:x2, :]


def from_rgb_to_grey(image: np.ndarray) -> np.ndarray:
    grey = 0.2989 * image[:, :, 0] + 0.5870 * image[:, :, 1] + 0.1140 * image[:, :, 2]
    grey = np.clip(grey, 0, 255)
    grey = grey.astype(np.uint8)
    return grey


def main() -> None:
    image: np.ndarray

    try:
        image = ft_load("image.jpeg")
        print(f"The shape of the image is: {image.shape}")
        image_zoomed = zoom_slice(image, 400, 400)
        grey = from_rgb_to_grey(image_zoomed)
        Image.fromarray(grey).show()
        print(f"New shape after slicing: {grey.shape} or {grey.shape[:2]}")
    except Exception as e:
        error_and_die(e)

    return


if __name__ == "__main__":
    main()
