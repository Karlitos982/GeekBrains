out_f = open("text_6.txt", "r", encoding="utf-8")
dict_pred = {}
for txt_str in out_f:
    a = txt_str.replace("-", "").replace("(пр)", "").replace("(л)", "").replace("(лаб)", "").replace("\n", "")
    out_str = a.split(": ")
    dict_pred[out_str[0]] = sum(list(map(lambda x: int(x), out_str[1].strip().split())))
print(dict_pred)
out_f.close()
