import re


def func(txt):
    return re.split(r'(?=[A-Z])', txt)

txt = input()
print(func(txt))
