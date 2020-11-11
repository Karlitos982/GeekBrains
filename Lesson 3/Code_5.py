def work():
    stroka = ""
    result = 0
    while True:
        if stroka.strip() == "0":
            print(f"ИТОГО: {result}")
            break
        elif stroka != "":
            print(f"Сумма введенных: {sum(B)}")
            print(f"Сумма общая: {result}")
            print("Закончить и показать итог - введите '0' или введите числа через пробел еще раз и нажмите ENTER")
        stroka = input(">> ")
        A = stroka.split()
        B = ((lambda x: [int(i) for i in x])(A))
        result += sum(B)


print("Введите несколько чисел через пробел и нажмите ENTER")
work()
