def volume_func(radius):
    volume = (4 / 3) * (3.14) * (radius ** 3)
    return volume

radius = float(input())
print(volume_func(radius))