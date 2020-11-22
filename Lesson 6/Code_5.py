class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки...")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        Stationery().draw()
        print("Инструмент - карандаш")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super(Pen, self).draw()
        print("Инструмент - ручка")
        

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        Stationery().draw()
        print("Инструмент - маркер")


#ins = Stationery("Инструмент")
#ins.draw()

pen = Pen("Красная ручка")
pen.draw()
