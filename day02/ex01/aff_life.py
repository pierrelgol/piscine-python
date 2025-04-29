#!/usr/bin/env python

import matplotlib.pyplot as plt
from load_csv import load


def main() -> int:
    """
    Load the life_expectancy_years.csv dataset and plot the
    life expectancy in France over time.
    """
    df = load("life_expectancy_years.csv")
    if df is None:
        print("Failed to load dataset.")
        return 1

    # select the France row (first column is 'country')
    france = df[df["country"] == "France"].iloc[0, 1:]
    # convert index from strings to ints for nicer x‐axis
    france.index = france.index.astype(int)

    # plot
    france.plot()
    plt.title("Life Expectancy in France (1800–2100)")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy (years)")
    plt.legend(["France"])
    plt.tight_layout()
    plt.show()
    return 0


if __name__ == "__main__":
    main()
