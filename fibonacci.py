from functools import reduce

def fibonacciList(n):
    #return [[0] * x for x in reduce(lambda x: )]
    a = ((0,1) for _ in range(n))    
    for w in a:
        print(w)   
    number = reduce(lambda x, n: [x[1], x[0] + x[1]], range(n), [0,1])[0]
    return [0] * number
    # return [[0] * x for x in range(number)]

print(fibonacciList(8))