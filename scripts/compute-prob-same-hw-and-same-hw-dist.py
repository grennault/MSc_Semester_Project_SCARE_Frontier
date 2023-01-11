# Author: Gaiëtan Renault
# Date: 2020-12-01
# Description: Compute the empirical probability that two states bytes after AK have the same Hamming weight AND the same Hamming distance with the corresponding bytes after Sbox.
# Usage: python3 compute-prob-same-hw-and-same-hw-dist.py
# Output around: 0.041

import math
import numpy as np


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


nbr_repeat = 10000
count = 0
count_2 = 0
i = 1

while i <= nbr_repeat:
    pt_state_1 = list(np.random.randint(low=0, high=256, size=(4 * 4)))
    pt_state_2 = list(np.random.randint(low=0, high=256, size=(4 * 4)))
    s_box = np.array([i for i in range(256)])
    np.random.shuffle(s_box)

    pt_state_1_hw = [number_to_hw(elem) for elem in pt_state_1]
    sb_state_1 = [s_box[elem] for elem in pt_state_1]
    sb_state_1_hw = [number_to_hw(s_box[elem]) for elem in pt_state_1]
    ham_dist_1 = [
        compute_hamming_distance(pt_state_1[i], sb_state_1[i]) for i in range(16)
    ]

    pt_state_2_hw = [number_to_hw(elem) for elem in pt_state_2]
    sb_state_2 = [s_box[elem] for elem in pt_state_2]
    sb_state_2_hw = [number_to_hw(s_box[elem]) for elem in pt_state_2]
    ham_dist_2 = [
        compute_hamming_distance(pt_state_2[i], sb_state_2[i]) for i in range(16)
    ]

    if np.sum(np.array(pt_state_1) == np.array(pt_state_2)) > 0:
        i -= 1
    else:
        val = 0
        j = 0
        for j in range(16):
            if ham_dist_1[j] == ham_dist_2[j] and sb_state_1_hw[j] == sb_state_2_hw[j]:
                val += 1
        if val > 0:
            count_2 += 1

        if ham_dist_1[0] == ham_dist_2[0] and sb_state_1_hw[0] == sb_state_2_hw[0]:
            count += 1
    i += 1
    print(
        f"Iter {i} : estimate : {count/i}\\Iter {i} : estimate : {count_2/i}", end="\r"
    )
