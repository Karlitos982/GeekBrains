text = input("Введите любое предложение: ").split()
counter = 0
for word in text:
    counter += 1
    if len(word) > 10:
        word = word[:10]
    print(f"{counter}. {word}")
