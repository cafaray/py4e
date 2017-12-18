from functools import reduce

def prefSum(a):
    return reduce(lambda mem, x: mem + [sum(mem[-1])], range(3), a[0])

a = [1, 2, 3]
print(prefSum(a))