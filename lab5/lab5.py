__author__ = "Artem Solbonov"
"""
=====================================================================
Даны натуральное число n, действительные числа a1,..., an. Вычислить:
a1**2 + ... + an**2;
=====================================================================
"""
import mod


def main():
    # number of digits
    n = int(input("Enter n:"))

    # arrays of digits from a1...an
    a_array = []

    # filling arrray with random numbers
    mod.filling_array(a_array, n)
    print(a_array)

    # degree calculation for each array element
    mod.calc_degree(a_array, 2)
    print(a_array)

# programm entry point
main()