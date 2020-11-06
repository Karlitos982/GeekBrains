# Использовал: tuple, list и dict
time_year = {"Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11], "Зима": [12, 1, 2]}
while True:
    dialog = input("Введите номер месяца (от 1 до 12): ")
    if dialog.isdigit():
        if (int(dialog) > 0) and (int(dialog)) < 13:
            break
    print(f"{dialog} - не является числом от 1 до 12, введите еще раз!")
for search_month in time_year.items():
    if int(dialog) in search_month[1]:
        print(search_month[0])
