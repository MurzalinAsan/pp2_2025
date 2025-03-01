import re

def func(txt):
    return ' '.join(re.findall(r'[A-Z][a-z]*', txt))

txt = "AbcdEfgHi"
print(func(txt))
