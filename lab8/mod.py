__author__ = "Artem Solbonov"

import random


def fill_list(arr: list):
    """Function that fills array with random number.1, 100 - number range"""
    for i in range(10):
        arr.append(random.randint(1, 20))


def find_even(arr: list):
    """Method that finds elements in list with even index sum"""
    elem_even_index = [] # Elements list with even index

    # Append element to list if sum of indexes is even
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (i + j) % 2 == 0:
                elem_even_index.append(arr[i][j])
    return elem_even_index


def find_equal(even: list, nums: list):
    """Method that finds elements from even array, that equal to nums array"""
    equal = [] # List for equal elements

    # Append element to list if equality between lists is true
    for i in range(len(even)):
        for j in range(len(nums)):
            if even[i] == nums[j]:
                # Adding to the list, only if there is no element in it
                if even[i] not in equal:
                    equal.append(even[i])
    return equal


def replace_equal(replc: list, matr: list):
    """Function that replace finded elements in matrix,
    with even indexes that equals to nums by zero in matrix"""
    for i in range(len(matr)):
        for j in range(len(matr)):
            for k in range(len(replc)):
                if matr[i][j] == replc[k]:
                    matr[i][j] = 0