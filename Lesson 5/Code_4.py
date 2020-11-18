def translate(old_txt):

    dict_number = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    for txt_str in old_txt:
        a = txt_str.split(" - ")
        new_txt_str = txt_str.replace(a[0], dict_number[a[0]])
        yield new_txt_str


old_f = open("text_4.txt", "r", encoding="utf-8")
new_f = open("out_file.txt", "w", encoding="utf-8")
for i_str in translate(old_f):
    new_f.write(i_str)
old_f.close()
new_f.close()
