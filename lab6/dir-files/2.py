import os

def function(path):
    print(os.path.exists(path))
    if os.path.exists(path):
        print(os.path.isdir(path))
        print(os.path.isfile(path))
        print(os.access(path, os.R_OK))
        print(os.access(path, os.W_OK))
        print(os.access(path, os.X_OK))
    else:
        print(f"{path} doesnt exist")


path = input()
function(path)

