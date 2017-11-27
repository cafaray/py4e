from itertools import dropwhile

pills = ["Notforgetan", "Antimoron", "Rememberin", "Bestmedicen", "Superpillsus"]

def memoryPills(pills):
    gen = dropwhile(lambda x: len(x)%2, pills + [""] *3)
    next(gen)
    return [next(gen) for _ in range(3)]

print(memoryPills(pills))