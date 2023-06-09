"""Даны целые числа a1, ..., a10, целочисленная квадратная матрица порядка n.
Заменить нулями в матрице те элементы с чётной суммой индексов, для которых
имеются равные среди a1, ..., a10
"""

__author__ = "Artem Solbonov"

import numpy as np
import mod as m


def main():
    nums = [] # Make empty list

    # Fill list with random numbers
    m.fill_list(nums)

    n = int(input("Matrix range: "))

    # Make n x n numpy array of ints between 0 and 20
    matr = np.random.randint(20, size=(n, n))

    # Get list of elements with even index sum
    even = m.find_even(matr)

    # Find replaceable elements which are equals among the nums
    equal = m.find_equal(even, nums)

    print(f"\nElements that shoul be replaced by zero: {equal}")
    print(f"\nMatrix before: \n{matr}\n")

    # Replace elements in matrix by zero, if they equal to elements from replc list
    m.replace_equal(equal, matr)

    print(f"Matrix after: \n{matr}") # Show matrix after replace operation
 
main()
