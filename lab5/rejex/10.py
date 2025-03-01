import re

def funct(txt):
    return re.sub(r'(?<!^)([A-Z])', r'_\1', txt).lower()


txt = "AbcDefGhi"
print(funct(txt))
