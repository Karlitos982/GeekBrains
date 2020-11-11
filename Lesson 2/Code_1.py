N = ["World!", 45, 12, 789, "RuhgYh", True, 3, False, "&&&", "4d4d4d4", 999, "float", "close", (1, 2, 3), [3, 2, 1]]
strok = 0
chisel = 0
mass = 0
n_mass = 0
boolean = 0

for i in range(len(N)):
    if type(N[i]) == str:
        strok += 1
    elif type(N[i]) == int:
        chisel += 1
    elif type(N[i]) == list:
        mass += 1
    elif type(N[i]) == tuple:
        n_mass += 1
    else:
        boolean += 1
print(f"ВСЕГО данных с типом: строка - {strok}, число - {chisel}, булево - {boolean}, списков - {mass}, "
      f"черепашек - {n_mass}")
