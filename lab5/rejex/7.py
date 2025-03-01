import re

def func(match):
    return match.group(1).upper()

def func2(snake):
    return re.sub(r'_([a-zA-Z])', func, snake)

snake = "hello_world_example"
camel = func2(snake)
print(camel)
