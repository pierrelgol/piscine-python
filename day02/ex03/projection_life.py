#!/usr/bin/env python

import sys
from typing import Any
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def orelse_unreachable(obj: Any | None, msg: str) -> Any:
    """
    Ensure that obj is not None; if it is, print an error and exit.

    Args:
        obj: The object to check.
        msg: Error message to display if obj is None.

    Returns:
        The original obj if not None.

    Exits:
        Program exits with status 1 if obj is None.
    """
    if obj is None:
        print(msg, file=sys.stderr)
        exit(1)
    return obj


def load_dataframe(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame, exiting on failure.

    Args:
        path: Path to the CSV file.

    Returns:
        A pandas DataFrame containing the loaded data.
    """
    return orelse_unreachable(load(path), f"failed to load {path}.")


def extract_data_from_year(df: pd.DataFrame, year: str) -> pd.Series:
    """
    Extract a single year's data from a DataFrame indexed by country.

    Args:
        df: DataFrame with a 'country' column and year columns.
        year: The year (column name) to extract.

    Returns:
        A pandas Series of values for the specified year, cast to float.
    """
    return orelse_unreachable(
        df.set_index("country")[year].astype(float),
        f"failed to extract {year} from DataFrame",
    )


def combine_series(
    label1: str, series1: pd.Series, label2: str, series2: pd.Series
) -> pd.DataFrame:
    """
    Combine two pandas Series into a single DataFrame with given column labels.

    Args:
        label1: Column name for the first Series.
        series1: The first pandas Series.
        label2: Column name for the second Series.
        series2: The second pandas Series.

    Returns:
        A pandas DataFrame with two columns labeled accordingly.
    """
    return orelse_unreachable(
        pd.DataFrame({label1: series1, label2: series2}),
        f"failed to combine series '{label1}' and '{label2}'",
    )


def remove_all_nan(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove any rows from the DataFrame that contain NaN values.

    Args:
        df: Input DataFrame.

    Returns:
        A DataFrame with all NaN-containing rows dropped.
    """
    return df.dropna()


def main() -> int:
    """
    Load GDP and life expectancy data for 1900,
    combine into a DataFrame, and plot a log-scaled scatter.

    Returns:
        0 on success.
    """
    # Load data
    gdp: pd.DataFrame = load_dataframe(
        "./income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    life: pd.DataFrame = load_dataframe("./life_expectancy_years.csv")

    # Extract 1900 data series
    gdp_1900: pd.Series = extract_data_from_year(gdp, "1900")
    life_1900: pd.Series = extract_data_from_year(life, "1900")

    # Combine into single DataFrame & drop missing
    df_1900: pd.DataFrame = combine_series(
        "gdp_per_capita", gdp_1900, "life_expectancy", life_1900
    )
    df_1900 = remove_all_nan(df_1900)

    # Plot setup
    figure: plt.Figure
    axis: plt.Axes
    figure, axis = plt.subplots()
    axis.scatter(
        df_1900["gdp_per_capita"],
        df_1900["life_expectancy"],
        s=40,
        alpha=1,
        label="Countries",
    )

    # Log scale and tick configuration
    axis.set_xscale("log")
    axis.set_xlim(300, 10_300)
    major_ticks = [300, 1_000, 10_000]
    axis.xaxis.set_major_locator(ticker.FixedLocator(major_ticks))
    axis.xaxis.set_minor_locator(
        ticker.LogLocator(base=10, subs=(2, 3, 4, 5, 6, 7, 8, 9), numticks=12)
    )
    axis.xaxis.set_minor_formatter(ticker.NullFormatter())

    # Formatter for major ticks
    def log_k_formatter(x: float, pos: int) -> str:
        if x >= 1000:
            k = x / 1000
            if k.is_integer():
                return f"{int(k)} k"
            return f"{k:.1f} k"
        return f"{int(x)}"

    axis.xaxis.set_major_formatter(ticker.FuncFormatter(log_k_formatter))

    # Labels and layout
    axis.set_title("1900")
    axis.set_xlabel("Gross domestic product")
    axis.set_ylabel("Life expectancy")
    plt.tight_layout()
    plt.show()
    return 0


if __name__ == "__main__":
    main()
