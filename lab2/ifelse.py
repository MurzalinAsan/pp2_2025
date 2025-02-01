x = 32
y = 30

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x and y are equal")


#or we can write it in a  shorter way: 
print("X") if x > y else print ("Y") if x < y else print("X=Y")

x = 40
y = 38
z = 31

if x > z and y > z:
    print("both conditions are true")


if x > z or x > y:
    print("one of the conditions or both of the conditions are true")
