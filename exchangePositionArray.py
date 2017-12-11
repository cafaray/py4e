def correctLineup(athletes):
    return [z for t in list(map(lambda x, y: (x, y), [athletes[x] for x in range(0, len(athletes)) if x%2!=0], [athletes[y] for y in range(0, len(athletes)) if y%2==0])) for z in t]

athletes = [2, 3, 1, 100, 99, 45, 22, 28]
print(correctLineup(athletes))