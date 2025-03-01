import re

pattern = r'\b[a-z]+_[a-z]+\b'

txt = ["hello_world", "absbd", "abc_def"]

for i in txt:
    if re.findall(pattern, i):
        print({i})