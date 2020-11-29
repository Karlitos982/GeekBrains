dohod = int(input("Введите доход фирмы: "))
rashod = int(input("Введите расход фирмы: "))
stuff = int(input("Введите численность сотрудников: "))
if dohod > rashod:
    print(f"Ваша фирма работает в плюс. Отношение выручки и издержек: {(dohod - rashod) / dohod * 100}%")
    print(f"Ваша прибыль, в расчете на 1 сотрудника: {(dohod - rashod) / stuff:.2f} у.е.")
