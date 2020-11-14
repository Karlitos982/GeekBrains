from sys import argv
print(f"{'*' * 5} Расчет заработной платы {'*' * 5}")
filename, hour, onehour, prem = argv
try:
    print("Отработанные часы: " + hour + ", ставка в час: " + onehour + ", примия: " + prem)
    print("Вычисляю... ", end="")
    print((int(hour) * int(onehour)) + int(prem))
except ValueError as err:
    print(err)
