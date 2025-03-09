import os


def func(path, ourpath):

    path1 = os.path.abspath(path)

    path2 = os.path.abspath(ourpath)
    if os.path.exists(path1) and os.path.commonpath([path1, path2]) == path2:
        os.remove(path1)
        print("del")

path = "../dir-files/f.py"
ourpath = "../dir-files"

func(path, ourpath)
    