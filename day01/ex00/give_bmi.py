#!/usr/bin/env python


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[float]:
    """This function returns a list of 'bmi'"""
    if not (isinstance(height, list) and isinstance(weight, list)):
        raise TypeError("Both height and weight must be lists.")
    if len(height) != len(weight):
        raise ValueError("height and weight must be the same length.")
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("Elements of height and weight must be int or float.")
        if h == 0:
            raise ValueError("Height cannot be zero.")
    return [w / (h**2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """This function returns a list of bool for each value in 'bmi 'if its above 'limit'"""
    if not isinstance(limit, int):
        raise TypeError("Limit must be an 'int'.")
    if not isinstance(bmi, list):
        raise TypeError("BMI basetype must be a 'list'.")
    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError("Elements of BMI must be 'int' or 'float'.")
    return [b > limit for b in bmi]
