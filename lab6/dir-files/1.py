import os

def func(path):
    x = os.listdir(path)

    dir = []
    file = []

    for i in x:
        ourpath = os.path.join(path, i)
        if os.path.isdir(ourpath):
            dir.append(i)
        elif os.path.isfile(ourpath):
            file.append(i)


    print(dir)
    print(file)
    print(x)


path = "../../lab6"
func(path)