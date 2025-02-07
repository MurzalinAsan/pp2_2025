class shape:
    def area(self):
        print(0)


class rectangle(shape):
    width = 0
    length = 0
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)

length = float(input("length:"))
width = float(input("width:"))

area = rectangle(length, width)
area.area()

shape = shape()
shape.area()






length = rectangle(float(input()))
length.area()

length = shape()
length.area()
