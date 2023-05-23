__author__ = "Артем Солбонов"

import random as rnd


def fill_list(n):
    """Метод, заполняющий список длиной n числами от 1 до 10"""
    mylist = [] # Список для возврата
    for i in range(n):
        mylist.append(rnd.randint(1, 10))
    return mylist


def pow_list(mylist, power):
    """Функция, возводящая каждый элемент списка mylist в степень power"""
    for i in range(len(mylist)):
        mylist[i] = mylist[i]**power