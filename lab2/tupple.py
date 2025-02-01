mytupple = ("bracelet", "laptop", "desk")
print(mytupple)

mytupple = ("bracelet", "laptop", "desk")
print(type(mytupple))

mytupple = ("bracelet", "laptop", "desk", "car")
print(mytupple[1:3])

mytupple = ("bracelet", "laptop", "desk")
if "laptop" in mytupple():
    print("YES")

mytupple = ("bracelet", "laptop", "desk")
y = list(mytupple)
y[1] = "car"
mytupple = tuple(y)

print(mytupple)


mytupple = ("bracelet", "laptop", "desk")
y = list(mytupple)
y.remove("bracelet")
mytupple = tuple(y)
print(mytupple)


mytupple = ("bracelet", "laptop", "desk")
(black, *gray) = mytupple
print(black)
print(gray)


mytupple = ("bracelet", "laptop", "desk")
i = 0
while i < len(mytupple):
    print(mytupple[0])
    i = i + 1


mytupple = ("bracelet", "laptop", "desk")
tuple2 = ("phone", "account")
tuple3 = mytupple + tuple2
print(tuple3)

mytupple1 = ("bracelet", "laptop", "desk")
mytupple2 = mytupple1*2
print(mytupple2)










