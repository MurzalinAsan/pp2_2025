import re

def func(t):
    pattern = r'[A-Z][a-z]*'
    m = []
    for i in t:
        if re.match(pattern, i):
            m.append(i)
    return m

t = ["Abcd", "adfg", "Hello", "kbtu"]
print(func(t))
