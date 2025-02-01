i = 1
while i < 8:
    print(i)
    i += 1


i = 2
while i <= 9:
    print(i)
    if i == 7:
        break
    i += 1

i = 3
while i < 10:
    i += 1
    if i == 8:
        continue
    print(i)


i = 4
while i < 123:
    print(i)
    i += 1
else:
    print("i has reached the point of 122")
