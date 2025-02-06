def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            print(chickens, rabbits)

numheads = int(input("Enter the amount of heads:"))
numlegs = int(input("ENter the amount of legs:"))
solve(numheads, numlegs)