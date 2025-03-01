import re


pattern = r'^a'

txt = ["aaab", "aaa", "basd", "aab"]

for i in txt:
    if re.findall(pattern, i):
        if re.findall("b$", i):
           print({i})