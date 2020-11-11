rating = [7, 5, 3, 3, 2]
while True:
    new = input("Введите число от 1 до 9: ")
    if new.isdigit():
        if (int(new) > 0) and (int(new)) < 10:
            break
    print(f"{new} - не является числом от 1 до 9, введите еще раз!")
for i in range(len(rating)):
    if int(new) >= rating[i]:
        rating.insert(i, int(new))
        break
    if i == len(rating) - 1:
        rating.append(int(new))
print(rating)
