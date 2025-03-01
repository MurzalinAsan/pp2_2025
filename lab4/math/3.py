import math


def area(n, s):
    print((n * s ** 2)/4 * math.tan(math.pi/n))


n = int(input())
s = int(input())

area(n, s)

