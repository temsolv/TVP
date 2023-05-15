# 15
#Даны гипотенуза и катет прямоугольного треугольника. Найти второй катет и радиус вписанной окружности.
__author__ = "Artem Solbonov"

import math


def find_cat(c, a):
    if a <= c:
        return math.sqrt(c**2-a**2)


c = float(input("Enter hyp: "))
if c < 0:
    exit("Invalid input")

a = float(input("Enter a: "))
if c < 0:
    exit("Invalid input")

b = (find_cat(c, a))
if b is None:
    print("cat can't be > hyp")
    exit

r = (a+b-c/2, 3)
print("\nCat: %.2f" % b)
print("Radius: %.2f" % r)
# print("Программа номер %2d, получила результат: %5.2f" % (4, 7.3333))

