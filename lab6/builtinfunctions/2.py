import string

def function(s: string):
    l = 0
    c = 0
    for i in s:
        if i.islower():
            l += 1
        elif i.isupper():
            c += 1


    print(l)
    print(c)

s = str(input())
function(s)

