#!/usr/bin/env python


def give_bmi(h8: list[int | float], w8: list[int | float]) -> list[int | float]:
    """This function returns a list of 'bmi'"""
    return [w / (h**2) for h, w in list(zip(h8, w8))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """This function returns a list of bool for each value in 'bmi 'if its above 'limit'"""
    results: list[bool] = []
    for i, b in enumerate(bmi):
        results.append(b > limit)
    return results
