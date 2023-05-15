# 115b
__author__ = "Artem Solbonov"


res = 0
k = 1
n = int(input("Enter n: "))
if n < 1:
    exit("Wrong input")

while k < n:
    res += 1/k**5
    k += 1

print(f"Result: {res:.4f}")
