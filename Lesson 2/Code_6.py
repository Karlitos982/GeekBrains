print(f"{'*' * 7} ЗАПОЛНЕНИЕ БАЗЫ ДАННЫХ ТОВАРАМИ {'*' * 7}")
trade = []
poz = ()
Z = {}
while True:
    print("Введите '+' для добавления информации о товаре;")
    print("Введите 'exit' или 'выход' для завершения... ")
    answer = input(">> ")
    if (answer.lower() == "exit") or (answer.lower() == "выход"):
        break
    if answer != "+":
        print(f"Команда {answer} - не распозана. Попробуйте еще раз!")
    else:
        counter = 0
        while True:
            counter += 1
            tovar_name = input("Введите название товара: ")
            Z["Название"] = tovar_name
            tovar_price = input("Введите стоимость товара: ")
            Z["Цена"] = tovar_price
            tovar_count = input("Введите количество товара: ")
            Z["Количество"] = tovar_count
            tovar_izm = input("Введите единицу измерения: ")
            Z["Ед. изм"] = tovar_izm
            poz = (counter, Z.copy())
            trade.append(poz)
            print("Добавить еще одну позицию товара?")
            print("'+' - да, ENTER - вывести аналитику и завершить работу программы...")
            answer_add = input(">> ")
            if answer_add != "+":
                name = []
                price = []
                count = []
                izm = []
                for st in trade:
                    name.append(st[1]["Название"])
                    price.append(st[1]["Цена"])
                    count.append(st[1]["Количество"])
                    izm.append(st[1]["Ед. изм"])
                analitics = {"Название": name, "Цена": price, "Количество": count, "Ед. изм": izm}
                print(analitics)
                break
        break
