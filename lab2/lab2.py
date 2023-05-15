__author__ = "Artem Solbonov"


def comprasion(a: int, b: int, c: int):
    return a < b < c


a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

res = comprasion(a, b, c)
print(res)
