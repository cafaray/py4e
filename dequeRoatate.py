from collections import deque
digits= [1, 2, 3, 4, 5]

def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda d, x: d.rotate(x), res, range(0, n)), 0)
    return [list(d) for d in res]

print(doodledPassword(digits))