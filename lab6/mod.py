__author__ = "Artem Solbonov"

import random

def fill_array(arr: list, size: int):
    """Function that fills array with random number. 1, 100 - number range"""
    for i in range(size):
        arr.append(random.randint(1, 100))


def find_aliquot(arr: list, a: int, b: int):
    """Function that finds numbers, that are at the same time multiples
    of a and non-multiples of b. Returns aliquot numbers array"""
    aliquot_arr = [] # array for aliquot numbers
    for i in range(len(arr)):
        if arr[i] % a == 0 and arr[i] % b != 0:
            aliquot_arr.append(arr[i])
    return aliquot_arr