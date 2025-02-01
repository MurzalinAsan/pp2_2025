def funct(a,b,c):
    return lambda x : a*x*x + b*x + c
y = funct(1,2,1)
print(y(11))