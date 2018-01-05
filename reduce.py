from itertools import accumulate

def prefSum(a):
    #print([sum(a[y:x]) for x in range(1, len(a)+1) for y in range(1)])
    #print([reduce(lambda x, y: x + y, a[0:z]) for z in range(1, len(a)+1)])
    
    print(list(accumulate(a)))
    #return reduce(lambda mem, x: mem + [sum(a[0:x])], a, range(len(a)))

a = [1, 2, 3]
#a = [1, 2, 3, -6]
#a = [0,0,0]
print(prefSum(a))