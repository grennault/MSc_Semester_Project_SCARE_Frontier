# Author: Gaiëtan Renault
# Date: 2020-12-01
# Description: Compute the empirical number of bytes that have after AK the same Hamming weight AND the same Hamming distance with the corresponding bytes after Sbox with any other plaintext byte. (for a random plaintext and given a random substitution table that the plaintext bytes are different)
# Usage: python3 compute-nbr-bytes-same-hw-same-dist-hw.py
# Output around: 211

import math
import numpy as np
from collections import Counter


def compute_hamming_distance(a, b):
    # Compute the Hamming weight of a XOR b
    return bin(a ^ b).count("1")


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
    raise Exception("Number too big")


nbr_repeat = 100000
count = 0
i = 1
res = [None for _ in range(256)]
hw_repartition = np.array([1, 8, 28, 56, 70, 56, 28, 8, 1])

print()
while i <= nbr_repeat:
    all_bytes = np.array([elem for elem in range(256)])
    s_box = np.array([elem for elem in range(256)])
    np.random.shuffle(s_box)

    all_bytes_hw = [number_to_hw(elem) for elem in all_bytes]
    sb_all_bytes = [s_box[elem] for elem in all_bytes]
    sb_all_bytes_hw = [number_to_hw(s_box[elem]) for elem in all_bytes]
    arg_sort_sb_all_bytes_hw = np.argsort(sb_all_bytes_hw)

    ham_dist_all_bytes = [
        compute_hamming_distance(all_bytes[elem], sb_all_bytes[elem])
        for elem in range(256)
    ]

    for j in range(256):
        res[j] = (
            all_bytes[arg_sort_sb_all_bytes_hw[j]],
            sb_all_bytes_hw[arg_sort_sb_all_bytes_hw[j]],
            ham_dist_all_bytes[arg_sort_sb_all_bytes_hw[j]],
        )

    val = 0
    min_ = 0
    max_ = 0
    for j in range(9):
        min_ = max_
        max_ += hw_repartition[j]
        set_ = set()
        list_ = []
        for k in range(min_, max_):
            set_.add(
                (
                    res[k][1],
                    res[k][2],
                )
            )
            list_ += [(res[k][1], res[k][2])]
        tmp = max_ - min_ - len(set_)
        val += tmp
        counter = Counter(list_)
        # print(counter)

    count += val
    i += 1
    print(f"Iter {i} : estimate : {count/i}", end="\r")

print(f"Iter {i} : estimate : {count/i}")
