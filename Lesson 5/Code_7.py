import json

with open("text_77.json", encoding="utf-8") as rd_obj:
    ser = json.load(rd_obj)
a = list(ser[0].values())
print(ser)
prib = 0
col = len(a)
for i in a:
    if i > 0:
        prib += i
    else:
        col -= 1
print("Прибыль:", prib, "среднее:", prib / col)

with open("test_77.json", "w", encoding="utf-8") as wr_obj:
    json.dump(ser, wr_obj)
