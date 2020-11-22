class Road:

    massa = 25 # Масса асфальта
    tolsch = 5 # необходимая толщина

    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        print("Параметры необходимой длянны и ширины заданы!")

    def asphalt(self):
        print("Рассчет необходимой массы асфальта...")
        print(f"Необходмимо: {int((self.__length * self.__width * self.massa * self.tolsch) / 1000)} тонн")


obj1 = Road(20, 5000)
obj1.asphalt()
