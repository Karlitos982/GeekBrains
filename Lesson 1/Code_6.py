a = int(input("Введите результат 1 дня: "))
b = int(input("Введите достигаемый результат: "))
counter = 0
result = a
while True:
    counter += 1
    print(f"{counter}-ый день: {result:.2f} км.")
    if result > b: break
    result = result + result * 0.1
