import os

l1 = []
a = int(input())

for i in range(a):
    x = input()
    l1.append(x)

f = open("prblm5.txt", "w")


for j in l1:
    f.write(j + "\n")


f.close()

