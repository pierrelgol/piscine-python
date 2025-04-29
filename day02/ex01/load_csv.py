#!/usr/bin/env python

import pathlib
import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """
    Load a CSV dataset into a pandas DataFrame.
    On success: prints its dimensions and returns the DataFrame.
    On failure (bad path or parse error): returns None.
    """
    path = pathlib.Path(path)
    if not path.is_file():
        return None

    try:
        df = pd.read_csv(path)
    except Exception:
        return None

    print(f"Loading dataset of dimensions {df.shape}")
    return df


def main() -> int:
    df = load("life_expectancy_years.csv")
    if df is None:
        print("Failed to load dataset.")
        return 1
    print(df)
    return 0


if __name__ == "__main__":
    main()
