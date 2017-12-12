from itertools import takewhile, count

def floatRange(start, stop, step):
    gen = takewhile(lambda x: x <= stop, count(start, step))
    return list(gen)

print(floatRange(-0.9, 0.45, 0.2))