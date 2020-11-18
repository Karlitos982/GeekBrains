def count_symbol_inline(file_txt):
    n = 0
    for txt_str in file_txt:
        n += 1
        print(f"{n}-я строка содержит {len(txt_str)} символов")


out_f = open("out_file_2.txt", "r", encoding="utf-8")
count_symbol_inline(out_f)
out_f.close()
