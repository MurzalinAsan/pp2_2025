import os

file = input()

f = open(file, "r")

x = f.readlines()

cnt = 0

for i in x:
    cnt += 1

print(cnt)