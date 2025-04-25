#!/usr/bin/env python

import pandas as pd
import pathlib as pl
import matplotlib.pyplot as plt
from PIL import Image
from load_csv import load
import numpy as np


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
        raise ValueError(f"ValueError: '{path.suffix}' extension is not supported")
    return plt.imread(path)


def main() -> int:
    df = load("./life_expectancy_years.csv")
    row = df[df.iloc[:, 0] == "France"].iloc[0]
    data = row.iloc[1:]
    data.plot(kind="line")
    plt.title("Data for France")
    plt.ylabel("Values")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("plot.jpeg")
    Image.fromarray(ft_load("./plot.jpeg")).show()

    return 0


if __name__ == "__main__":
    main()
