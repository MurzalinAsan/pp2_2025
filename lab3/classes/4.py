class point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print("x: " , self.x ,"," , "y: " , self.y)
    def move(self, x2, y2):
        self.x = x2
        self.y = y2
        print(self.x, self.y)
    def dist(self, x3, y3):
        self.x3 = x3
        self.y3 = y3
        return (abs(self.x - self.x3) ** 2 + abs(self.y - self.y3) ** 2) ** 0.5
    
x = float(input())
y = float(input())

mypoint = point(x, y)
mypoint.show()
x2 = float(input())
y2 = float(input())
newpoint = point(x2, y2)
newpoint.move(x2, y2)