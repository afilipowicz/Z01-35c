import sys
import os

args = sys.argv
path = args[1]

spacer = " "

def listContents(path, count = 0, recursively = True):
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():
                prettyPrint(entry.name, count)
                count += 2
                listContents(entry.path, count)
                count -= 2
            else:
                prettyPrint(entry.name, count)

def prettyPrint(string, count):
    print(f"{spacer * count}{string}")

listContents(path)
