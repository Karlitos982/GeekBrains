n = int(input("Введите время в секундах: "))
h = n // 3600
m = (n // 60) % 60
s = n % 60
print("{:0=2d}:{:0=2d}:{:0=2d}".format(h, m, s))

