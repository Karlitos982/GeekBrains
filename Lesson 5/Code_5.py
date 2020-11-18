from random import randint


def generate_file():
    file_str = ""
    out_f = open("text_5.txt", "w", encoding="utf-8")
    for i in range(1, randint(1, 20)):
        file_str += str(randint(1, 100)) + " "
    out_f.write(file_str)
    out_f.close()


def write_file():
    out_f = open("text_5.txt", "r", encoding="utf-8")
    file_list = list(map(lambda x: int(x), out_f.read().split()))
    print("Сумма чисел в файле:", sum(file_list))
    out_f.close()


generate_file()
write_file()
