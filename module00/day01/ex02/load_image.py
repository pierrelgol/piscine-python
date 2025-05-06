#!/usr/bin/env python

import matplotlib.pyplot as pyplot
import numpy as np
import pathlib as pl


def ft_load(path: str) -> np.ndarray:
    """
    This function loads an image as a 'numpy.ndarray'
    and raises a ValueError if:
        - The path is not a valid path.
        - The path is not a file.
        - The path access is priviledged.
        - The path format extension is not supported.
    """
    path = pl.Path(path)
    if not path.exists() or not path.is_file():
        raise ValueError(f"ValueError: '{path}' is not a valid path.")
    if path.suffix not in {".jpeg", ".jpg"}:
        raise ValueError(f"ValueError: '{path.suffix}' format not supported")
    image = pyplot.imread(path)
    print(np.shape(image))
    return image
