out_f = open("out_file.txt", "w", encoding="utf-8")
print("Введите необходимую информацию для записи в файл или пустую строку ")
while True:
    text = input(">>> ").strip()
    if text == "":
        break
    out_f.write(text + "\n")
out_f.close()
