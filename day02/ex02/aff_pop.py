#!/usr/bin/env python

import sys
from typing import Any, Generator
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def orelse_unreachable(obj: Any | None, msg: str) -> Any:
    """
    Ensure that obj is not None, otherwise exit with error.

    Args:
        obj: The object to check for None.
        msg: An error message to print if obj is None.

    Returns:
        The original obj if it is not None.

    Exits:
        Terminates program with status 1 if obj is None.
    """
    if obj is None:
        print(msg, file=sys.stderr)
        exit(1)
    else:
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


def create_range_of_years(
    from_y: int, to_y: int, step_y: int
) -> Generator[int, None, None]:
    """
    Create a generator of years from start to end (exclusive) with a given step.

    Args:
        from_y: The starting year (inclusive).
        to_y: The ending year (exclusive).
        step_y: Step size between consecutive years.

    Returns:
        A generator that yields integers from from_y to to_y-1 by step_y.
    """
    return (y for y in range(from_y, to_y, step_y))


def create_list_of_years_from_range(years: Generator[int, None, None]) -> list[str]:
    """
    Convert a generator of integer years into a list of string representations.

    Args:
        years: A generator yielding integer year values.

    Returns:
        A list of years as strings.
    """
    return [str(y) for y in years]


def parse_dataframe_population(df: pd.DataFrame, years: list[str]) -> pd.DataFrame:
    """
    Parse population values in a DataFrame that use suffixes (e.g., 'M', 'k') into floats.

    Args:
        df: Original DataFrame with population columns as strings.
        years: List of column names (year strings) to parse.

    Returns:
        A new DataFrame with the specified year columns converted to numeric floats.
    """

    def parse_cell(cell: Any) -> float:
        """
        Convert a single cell containing a population with suffix to float.

        Args:
            cell: Cell value, possibly a string like '3.28M' or an already numeric value.

        Returns:
            A float representing the numeric population.
        """
        suffix_map = {"B": 1_000_000_000, "M": 1_000_000, "k": 1_000}

        if not isinstance(cell, str):
            return float(cell)

        cell_str = cell.strip()
        if not cell_str:
            return float("nan")

        unit = cell_str[-1]
        if unit in suffix_map:
            number = float(cell_str[:-1])
            return number * suffix_map[unit]
        else:
            return float(cell_str)

    clone = df.copy()
    clone[years] = clone[years].applymap(parse_cell)
    return clone


def extract_countries_data_in_range(df: pd.DataFrame, years: list[str]) -> pd.DataFrame:
    """
    Extract a subset of the DataFrame containing only the specified years,
    indexed by country.

    Args:
        df: DataFrame with a 'country' column and year-columns.
        years: List of year column names to extract.

    Returns:
        A DataFrame indexed by country, containing only the specified years.
    """
    return orelse_unreachable(
        df.set_index("country")[years], f"Failed to extract countries in range {years}"
    )


def get_serie_for_country(df: pd.DataFrame, name: str) -> pd.Series:
    """
    Retrieve the population series for a given country from a DataFrame.

    Args:
        df: DataFrame indexed by country with year-columns.
        name: Country name to retrieve.

    Returns:
        A pandas Series of population values for the specified country.
    """
    return orelse_unreachable(df.loc[name], f"Failed to get serie from {name}")


def main() -> int:
    """
    Main entrypoint: load population data, parse it, extract two countries,
    and plot their population projections from 1800 to 2050.

    Returns:
        0 on success, 1 on failure.
    """
    dataframe: pd.DataFrame = load_dataframe("./population_total.csv")

    country1: str = "France"
    country2: str = "Belgium"

    yearly_range: Generator[int, None, None] = create_range_of_years(1800, 2051, 1)
    years_list: list[str] = create_list_of_years_from_range(yearly_range)
    dataframe = parse_dataframe_population(dataframe, years_list)
    dataframe_sub: pd.DataFrame = extract_countries_data_in_range(dataframe, years_list)

    population_1: pd.Series = get_serie_for_country(dataframe_sub, country1)
    population_2: pd.Series = get_serie_for_country(dataframe_sub, country2)
    population_1.index = population_1.index.astype(int)
    population_2.index = population_2.index.astype(int)

    figure: plt.Figure
    axis: plt.Axes
    figure, axis = plt.subplots()
    axis.plot(population_1.index, population_1.values, label=country1, color="green")
    axis.plot(population_2.index, population_2.values, label=country2, color="blue")
    axis.set_title("Population Projections")
    axis.set_xlabel("Year")
    axis.set_ylabel("Population")
    axis.legend(loc="lower right")

    axis.set_xticks(range(1800, 2051, 40))
    axis.xaxis.set_tick_params(rotation=45)
    axis.yaxis.set_major_locator(ticker.MaxNLocator(nbins=4, integer=True))
    axis.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, pos: f"{int(x / 1e6)}M")
    )

    plt.tight_layout()
    plt.show()
    return 0


if __name__ == "__main__":
    main()
