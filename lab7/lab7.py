__author__ = "Artem Solbonov"
"""334a. Вычислить Σi=1...100:Σj=1...50:1/i+j**2"""
import mod


def main():
    """Programm main method"""
    # finding the sum by given formula
    res = mod.find_sum(100, 50)
    
    # sum result output
    print(res)


# programm entry point
main()