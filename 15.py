x = 2 #int
y = 3.1 #float
z = 1j #complex

#Type conversion

a = float(x) #from int to float

b = int(y) #from float to int

c = complex(x) #from int to complex

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Importing the random module and displaying a random number

import random
print(random.randrange(1, 15))

