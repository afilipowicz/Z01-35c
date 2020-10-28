import sys
import os

args = sys.argv
path = args[1]

spacer      = "    "
lineSpacer  = "│   "
middle      = "├───"
end         = "└───"

def printContents(path, buffer = list()):
    for entry, isLast in preview(os.scandir(path)):
        prettyPrint(entry.name, buffer, isLast)

        if entry.is_dir():
            buffer.append(isLast)
            printContents(entry.path, buffer)
    if buffer:
        buffer.pop()

def prettyPrint(name, buffer, isLast = False):
    spacers = "".join(map(bufferToSpacers, buffer))
    lastElement = end if isLast else middle
    print(f"{spacers}{lastElement}{name}")

def bufferToSpacers(element):
    return lineSpacer if element == False else spacer

def preview(iterable):
    iterator = iter(iterable)
    try:
        current = next(iterator)
    except StopIteration:
        return

    for el in iterator:
        yield current, False
        current = el
    yield current, True

printContents(path)
