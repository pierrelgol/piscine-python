#!/usr/bin/env python

from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15, {"02": 43, "i9302": 43}]
weight = [165.3, 38.4, "abc", "def", "hij"]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
