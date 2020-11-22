from tkinter import *
import time


class TrafficLights:
    __color = "red"

    def __init__(self):
        window = Tk()
        window.title("Traffic Light")
        frame = Frame(window)
        frame.pack()

        self.__info = StringVar()
        self.__info.set("Нажмите кнопку для запуска светофора...")

        self.canvas = Canvas(window, width=350, height=150, bg="white")
        self.canvas.pack()

        self.oval_red = self.canvas.create_oval(10, 10, 110, 110, fill="white")
        self.oval_yellow = self.canvas.create_oval(120, 10, 220, 110, fill="white")
        self.oval_green = self.canvas.create_oval(230, 10, 330, 110, fill="white")

        ButtonClk = Button(frame, text="Запустить", command=self.running)
        ButtonClk.grid(row=10, column=1, sticky="nsew")
        label1 = Label(frame, textvariable=self.__info, bg="lightgray", fg="blue")
        label1.grid(row=1, column=1)

        window.mainloop()

    def running(self):
        self.__info.set("Красный")
        self.canvas.itemconfig(self.oval_red, fill="red")
        self.canvas.update()
        time.sleep(7)
        self.canvas.itemconfig(self.oval_red, fill="white")
        self.canvas.itemconfig(self.oval_yellow, fill="yellow")
        self.canvas.itemconfig(self.oval_green, fill="white")
        self.__info.set("Желтый")
        self.canvas.update()
        time.sleep(2)
        self.canvas.itemconfig(self.oval_red, fill="white")
        self.canvas.itemconfig(self.oval_yellow, fill="white")
        self.canvas.itemconfig(self.oval_green, fill="green")
        self.__info.set("Зеленый")
        self.canvas.update()
        time.sleep(7)
        self.canvas.itemconfig(self.oval_red, fill="white")
        self.canvas.itemconfig(self.oval_yellow, fill="white")
        self.canvas.itemconfig(self.oval_green, fill="white")
        self.canvas.update()
        self.__info.set("Нажмите еще раз для запуска светоформа!")


TrafficLights()