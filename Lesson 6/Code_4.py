class Car:
    def __init__(self, name, color, speed):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = False

    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed} км/ч")
        if self.speed < 1:
            print("Машина остановлена!")

    def up_speed(self):
        self.speed += 10
        print(f"Скорость увеличена на 10 км/ч")
        self.show_speed()

    def down_speed(self):
        self.speed -= 10
        print(f"Скорость снижена на 10 км/ч")
        self.show_speed()

    def go(self):
        print(f"Машина {self.name} поехала!")

    def stop(self):
        print(f"Машина {self.name} тормозит...", end="")
        self.speed = 0
        self.show_speed()

    def turn(self, direction):
        print(f"Машина {self.name} повернула на {direction}")


class TownCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed}")
        if self.speed < 1:
            print("Машина остановлена!")
        elif self.speed > 60:
            print("Ваша скорость выше 60 км/ч! Сбросьте скорость...")


class WorkCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed}")
        if self.speed < 1:
            print("Машина остановлена!")
        elif self.speed > 40:
            print("Ваша скорость выше 40 км/ч! Сбросьте скорость...")


class SportCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed}")
        if self.speed < 1:
            print("Машина остановлена!")
        elif self.speed < 60:
            print("Зачем Вам спорткар, если Вы так медленно ездите? Прибавьте газу!")

    def up_speed(self):
        self.speed += 30
        print(f"Скорость увеличена на 30 км/ч")
        self.show_speed()

    def down_speed(self):
        self.speed -= 30
        print(f"Скорость снижена на 30 км/ч")
        self.show_speed()


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)
        self.is_police = True


# Объект базового класса:
Car1 = Car("Калина", "Желтый", 55)
Car1.go()
Car1.show_speed()
Car1.up_speed()
Car1.turn("право")
Car1.stop()
print("_" * 10)

# Объекты дочерних классов:
Car2 = TownCar("Daewoo Nexia", "Серо-голубой", 55)
Car2.go()
Car2.show_speed()
Car2.up_speed()
Car2.turn("лево")
Car2.stop()
print("_" * 10)

Car3 = WorkCar("Renault logan", "Черный", 45)
Car3.go()
Car3.show_speed()
Car3.down_speed()
Car3.stop()
print("_" * 10)
