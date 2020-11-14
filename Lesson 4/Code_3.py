from random import randint
b = [i for i in [randint(1, 240) for i in range(20, 240)] if i % 20 == 0 or i % 21 == 0]
print(b)
