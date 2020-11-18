def file_summary(txt_file):
    list_zp = []
    print("Оклад менее 20 000₽ у следующих сотрудников: ")
    for txt_str in txt_file:
        a = txt_str.replace("\n", "").split(" ")
        if float(a[1]) < 20000:
            print(a[0] + ";", end=" ")
        list_zp.append(float(a[1]))
    return sum(list_zp) / len(list_zp)


out_f = open("text_3.txt", "r", encoding="utf-8")
print(f"{file_summary(out_f)}₽ - средняя зарплата у работников.")
out_f.close()
