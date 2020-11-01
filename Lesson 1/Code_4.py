n = int(input("Введите число: "))
maximum = 0
while n > 0:
    maximum = max(maximum, n % 10)
    n //= 10
print(f"Самая большая цифра: {maximum}")