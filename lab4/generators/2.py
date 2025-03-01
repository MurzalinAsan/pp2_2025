def evennum(N):
    x = 0

    while x <= N:
        if x % 2 == 0:
            yield x
        x += 1


N = int(input())
for i in evennum(N):
    print(i)