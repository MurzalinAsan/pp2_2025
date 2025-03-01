def sqr(N):
    x = 0

    while x <= N:
        y = x ** 2
        yield y
        x += 1


N = int(input())
for  i in sqr(N):
    print(i)

    



