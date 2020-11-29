class MyClass:
    def __init__(self, V, H):
        self.V = V
        self.H = H

    @property
    def my_method(self):
        return f"Параметры, переданные в класс:" \
            f" {self.param_1}, {self.param_2}"


mc = MyClass("text_1", "text_2")

print(mc.param_1)
print(mc.param_2)

print(mc.my_method)