""" Дано натуральное число n <= 100, определяющее возраст человека (в годах)
Дать для этого числа наименования "год", "года", или "лет": например, 1 год,
23 года, 45 лет и т.д. """

__author__ = "Artem Solbonov"


def exception_check(n: int, arr: list):
    for i in range(len(arr)):
        if n == arr[i]:
            return True


n = int(input("Введите n:"))
exception_years = [11, 12, 13, 14]
is_exception = exception_check(n, exception_years)

if n > 100:
    exit()
elif is_exception != None:
    print(n, "лет")
elif n % 10 == 1:
    print(n, "год")
elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
    print(n, "года")
else:
    print(n, "лет")
