import re

def func(txt):
    pattern = r"( |,|\.)"
    x = ''
    for i in txt:
        if re.match(pattern, i):
            x += ':'
        else:
            x += i
    return x


txt = "abcd , efg. hi"
print(func(txt))
