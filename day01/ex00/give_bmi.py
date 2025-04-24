#!/usr/bin/env python

# from typing import List, Tuple


def give_bmi(h8: list[int | float], w8: list[int | float]) -> list[int | float]:
    return [w / (h**2) for h, w in list(zip(h8, w8))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return list(map(lamda x))
