from functools import reduce

def mathPractice(numbers):
    e = enumerate(numbers)
    for i in e:
        print(i)
    return reduce(lambda x, i: x+i[1] if i[0] % 2 else x * i[1], enumerate(numbers), 1)


numbers = [1, 2, 3, 4, 5, 6]
print(mathPractice(numbers))