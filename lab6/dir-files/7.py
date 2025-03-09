import os

f = open("prblm7.txt", "r")
g = open("prblm7_1.txt", "w")

g.write(f.read())

f.close()
g.close()