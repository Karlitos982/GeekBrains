N = []
a = None
while len(N) < 2 or a != 0:
    a = input("Введите значение для создания списка или 0 для завершения: ")
    if a == "0":
        if len(N) < 2:
            print("Введите не менее 2-х элементов!")
            continue
        else:
            break
    N.append(a)
print(N)
for i in range(0, len(N), 2):
    if i + 2 <= len(N):
        N[i + 1], N[i] = N[i], N[i + 1]
print(N)
