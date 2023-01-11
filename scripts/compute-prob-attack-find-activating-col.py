# Author: Gaiëtan Renault
# Date: 2020-12-01
# Description: Compute the empirical probability that that attack find the 4 bytes (up to permutation) activating same column in first try
# Usage: python3 compute-prob-attack-find-activating-col.py
# Output around: 0.90

import math
import numpy as np


def number_to_hw(nbr):
    if nbr == 0:
        return 0
    if nbr <= 8:
        return 1
    if nbr <= 8 + 28:
        return 2
    if nbr <= 8 + 28 + 56:
        return 3
    if nbr <= 8 + 28 + 56 + 70:
        return 4
    if nbr <= 8 + 28 + 56 + 70 + 56:
        return 5
    if nbr <= 8 + 28 + 56 + 70 + 56 + 28:
        return 6
    if nbr <= 8 + 28 + 56 + 70 + 56 + 28 + 8:
        return 7
    if nbr <= 255:
        return 8


nbr_repeat = 1000000
count = 0

for i in range(1, nbr_repeat + 1):
    print(f"Iter {i} : estimate : {1 - count/(i+1)}", end="\r")
    a = list(np.random.randint(low=0, high=256, size=(4 * 4)))
    a = [number_to_hw(elem) for elem in a]
    first_col_set = set(a[:4])
    second_col_set = set(a[4:8])
    third_col_set = set(a[8:12])
    fourth_col_set = set(a[12:])
    if first_col_set in [second_col_set, third_col_set, fourth_col_set]:
        count += 1

print(1 - count / nbr_repeat)
