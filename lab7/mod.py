__author__ = "Artem Solbonov"


def find_sum(a:int, b:int):
    """Calculation of the sum according to a given formula, a and b - cycle boundaries.
    Checks parameters in input"""
    
    # calculation result
    res = 0
    for i in range(1, a):
        for j in range(1, b):
            # adding res to itself each iteration
            res += 1/(i+j**2)
    return res