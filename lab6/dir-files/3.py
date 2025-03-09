import os

def function(path):
    if os.path.exists(path):
        print(os.path.basename(os.path.abspath(path)))
        print((os.path.dirname(os.path.abspath(path))))

    else:
        print("does not exist")

path = input()
function(path)