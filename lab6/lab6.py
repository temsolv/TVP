__author__= "Artem Solbonov"
"""
Даны натуральные числа n, a1...an. Определить количество членов
ak последовательности a1,...,an: кратных 3 и не кратных 5
"""
import mod


def main():
    n = int(input("Array elements number: ")) # array size
    initial_arr = [] # initial array
    aliqout_arr = [] # alilquot numbers array

    # filling array with random numbers
    mod.fill_array(initial_arr, n)

    # aliquot of 3 and non aliquot of 5 search
    aliquot = 3
    no_aliquot = 5
    aliquot_arr = mod.find_aliquot(initial_arr, aliquot, no_aliquot)

    # result output
    print(f"\nInitial array: {initial_arr}")
    print(f"Aliquot {aliquot}, non aliquot {no_aliquot} array: {aliquot_arr}\n")


main()