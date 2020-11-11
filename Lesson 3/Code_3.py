def max_elements(el_1, el_2, el_3):
    summ = 0
    spisok = [el_1, el_2, el_3]
    for i in spisok:
        if i != min(spisok):
            summ += i
    return summ


elem1 = input("Введите 1-е число: ")
elem2 = input("Введите 2-е число: ")
elem3 = input("Введите 3-е число: ")

try:
    elem1 = float(elem1)
    elem2 = float(elem2)
    elem3 = float(elem3)
    summ = max_elements(elem1, elem2, elem3)
    print(f"Сумма наибольших чисел: {summ}")
except ValueError:
    print("Ошибка! Вы уверены, что ввели именно числа?")

