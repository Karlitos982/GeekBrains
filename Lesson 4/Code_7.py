def almost_factorial(n):
    N_fact = 1

    for i in range(1, n + 1):
        N_fact *= i
        yield N_fact


gen = almost_factorial(int(input("Какого числа факториал? ")))
for el in gen:
    print(el)
