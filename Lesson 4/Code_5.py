from functools import reduce
from random import randint


def my_func(prev_el, el):
    return prev_el * el


old_list = [i for i in range(100, 1001) if i % 2 == 0]
print(old_list)
print(reduce(my_func, old_list))
