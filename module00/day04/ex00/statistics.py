#!/usr/bin/env python

from typing import Any, List


def compute_median(items: List[float]) -> float:
    """
    Compute the median of a sorted list of numbers.

    Args:
        items (List[float]): A sorted list of numeric values.

    Returns:
        float: The median value.
    """
    length = len(items)
    mid = length // 2
    return items[mid] if length & 1 else (items[mid - 1] + items[mid]) / 2


def compute_quartiles(data: List[float]) -> List[float]:
    """
    Compute the first and third quartiles (Q1 and Q3) of a list of numbers.

    Args:
        data (List[float]): A list of numeric values.

    Returns:
        List[float]: A list containing Q1 and Q3.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)

    mid = n // 2
    if n % 2 == 0:
        lower_half = sorted_data[:mid]
        upper_half = sorted_data[mid:]
    else:
        lower_half = sorted_data[:mid]
        upper_half = sorted_data[mid + 1 :]

    q1 = compute_median(lower_half)
    q3 = compute_median(upper_half)
    return [q1, q3]


def compute_variance(data: List[float]) -> float:
    """
    Compute the variance of a list of numbers.

    Args:
        data (List[float]): A list of numeric values.

    Returns:
        float: The variance of the data.
    """
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / n


def compute_standard_deviation(data: List[float]) -> float:
    """
    Compute the standard deviation of a list of numbers.

    Args:
        data (List[float]): A list of numeric values.

    Returns:
        float: The standard deviation.
    """
    var = compute_variance(data)
    return var**0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Print statistical metrics requested via kwargs on the input numeric args.

    Supported metrics via kwargs values:
        - "mean"
        - "median"
        - "quartile"
        - "var"
        - "std"

    Args:
        *args: A variable number of numeric values.
        **kwargs: Keyword arguments specifying which statistics to compute.
    """
    if not args:
        print("ERROR")
        return

    numbers: List[float] = []
    try:
        numbers = [float(x) for x in args]
    except (TypeError, ValueError):
        print("ERROR")
        return

    if not kwargs:
        print("ERROR")
        return

    for key, value in kwargs.items():
        if value == "mean":
            print(f"{value} : {sum(numbers) / len(numbers)}")
        elif value == "median":
            print(f"{value} : {compute_median(numbers)}")
        elif value == "quartile":
            print(f"{value} : {compute_quartiles(numbers)}")
        elif value == "var":
            print(f"{value} : {compute_variance(numbers)}")
        elif value == "std":
            print(f"{value} : {compute_standard_deviation(numbers)}")
        else:
            print("ERROR")


def main() -> None:
    """
    Entry point for testing ft_statistics with various inputs.
    """
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
