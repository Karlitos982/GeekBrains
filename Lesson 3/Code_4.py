def degree(a, b):
    A = a
    for i in range(0, int(b) - 1, -1):
        A *= (1 / a)
    print(round(A, 2))


print("Введите числа..")

while True:
    try:
        x = float(input("..действительное положительное: "))
        if x > 0:
            break
        print("Это отрицательное число!")
    except ValueError:
        print("Это не число!")

while True:
    try:
        y = float(input("..целое отрицательное: "))
        if y < 0:
            if y.is_integer():
                break
            print("Это не целое число!")
        else:
            print("Это положительное число!")
    except ValueError:
        print("Это не число!")
degree(x, y)
