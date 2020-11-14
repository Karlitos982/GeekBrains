from random import randint
a = randint(10, 20)
lst = [randint(1, 10) for i in range(a)]
print("Сгенерированный список: ", lst)
sp = []
for i in range(len(lst)):
    if i > 0 and lst[i] > lst[i - 1]:
        sp.append(lst[i])
print("Получившийся список: ", sp)
