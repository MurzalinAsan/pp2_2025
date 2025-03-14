import string

def f(s:string):
    c = "".join(reversed(s))

    if s == c:
        return True
    else:
        return False
    
s = str(input())
print(f(s))