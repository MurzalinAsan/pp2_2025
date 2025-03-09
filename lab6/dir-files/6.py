import os

for i in range(ord('A'), ord('Z') + 1):
    fname = chr(i) + ".txt"
    f = open(fname, "x")
    f.close()