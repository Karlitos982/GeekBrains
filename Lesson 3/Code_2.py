def user_info(a, b):
    c = ""
    for i in range(len(a)):
        c = c + a[i] + ": " + b[a[i]] + "; "
    print(c)


user_data = {}
data = ["Фамилия", "Имя", "Отчество", "Год рождения", "Город проживания", "Телефон", "E-MAIL"]
print("Введите следующую информацию о себе")
for i in data:
    user_data[i] = input(f"{i}: ")
user_info(b=user_data, a=data)
