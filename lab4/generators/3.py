def divis(N):

    for i in range(N + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


N = int(input())

for i in divis(N):
    print(i)