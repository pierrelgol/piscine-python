#!/usr/bin/env python

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    This function that takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start and end arguments.
    """
    if family is None or not isinstance(family, list) or np.ndim(family) != 2:
        return None
    print(f"My shape is : {np.shape(family)}")
    reshaped = family[start:end]
    print(f"My new shape is : {np.shape(reshaped)}")
    return reshaped
