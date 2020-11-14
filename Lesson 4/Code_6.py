from itertools import count, cycle

a = int(input("Введите точку старта: "))
A = []
for el in count(a):
    if el > 10:
        break
    else:
        A.append(el)
print(A)
с = 0
for el in cycle(A):
    if с > 20:
        break
    print(el)
    с += 1
