spacer      = "    "
lineSpacer  = "│   "
middle      = "├───"
end         = "└───"

def printContents(characters, buffer = list()):
    for e, isLast in preview(characters):
        isList = isinstance(e, list)
        prettyPrint(e[0] if isList and len(e) > 1 else e, buffer, isLast)

        if isList:
            buffer.append(isLast)
            printContents(e[1:], buffer)
    if buffer:
        buffer.pop()

def prettyPrint(name, buffer, isLast = False):
    spacers = "".join(map(bufferToSpacers, buffer))
    lastElement = end if isLast else middle
    print(f"{spacers}{lastElement} {name}")

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
