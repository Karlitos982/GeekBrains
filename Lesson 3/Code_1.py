def division(del1, del2):
    try:
        return float(del1) / float(del2)
    except ZeroDivisionError:
        return "Ошибка! Деление на ноль невозможно!"
    except ValueError as err:
        return err


a = input("Введите делимое: ")
b = input("Введите делитель: ")
print(division(a, b))
