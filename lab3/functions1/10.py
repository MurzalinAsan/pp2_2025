def unique(x1):
    x2 = sorted(x1)
    y = []
    for i in range(len(x1) - 1):
        if x2[i] != x2[i + 1]:
            y.append(x2[i])
    y.append(x2[len(x2) - 1])
    print(y)