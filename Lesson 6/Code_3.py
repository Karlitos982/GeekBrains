class Worker:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.position = "Депутат"
        self._income = {"Oklad": 60000, "Premia": 10000}


class Position(Worker):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def get_full_name(self):
        print(f"Имя сотрудника: {self.name + ' ' + self.surname}")

    def get_total_income(self):
        print(f"Зарплата сотрудника в должности '{self.position}': {sum(self._income.values())} руб.")


person = Position("Иван", "Иванов")
person.get_full_name()
person.get_total_income()
