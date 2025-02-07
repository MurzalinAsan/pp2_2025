n = [x for x in range(-20, 140)]
prime = list(filter(
    lambda r: False if r < 2 else all([r % x != 0 for x in range(2, int(r ** 0.5 + 1))]), n
))

print(prime)