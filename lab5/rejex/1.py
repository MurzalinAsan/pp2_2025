import re

pattern = r"^ab*$"

txt = ["a", "ab", "abb", "abbb", "b", "ba", "abc", "aab"]


for i in txt:
    if re.fullmatch(pattern, i):
        print({i})