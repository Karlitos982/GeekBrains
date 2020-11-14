from random import randint
a = randint(10, 20)
old_list = [randint(1, 10) for i in range(a)]
new_list = [item for item in old_list if old_list.count(item) == 1]
print(old_list)
print(new_list)
