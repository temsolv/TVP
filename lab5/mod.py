__author__ = "Artem Solbonov"

import random


def filling_array(arr: list, size: int):
    """Function that fills array with random number. 1, 10 - digit range"""
    for i in range(size):
        arr.append(random.randint(1, 10))


def calc_degree(arr: list, degree: int):
    """Function that calculate degree of each numbers, takes arr and degree,
    replace each element by same element in selected degree"""
    for i in range(len(arr)):
        arr[i] = (arr[i])**degree