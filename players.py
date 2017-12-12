#from itertools import permutations

#def rockPaperScissors(players):
#    return list(permutations(players, 2))

#p = ["trainee", "warrior", "ninja"]
#print(rockPaperScissors(p))


#from itertools import permutations

#def kthPermutation(numbers, k):
#    return list(list(permutations(numbers, len(numbers)))[k-1])

#numbers = [1, 2, 3, 4, 5]
#print(kthPermutation(numbers, 4))

#from itertools import combinations

#def crazyball(players, k):
#    return list(list(combinations(sorted(players), k)))

#players = ["Ninja", "Warrior", "Trainee", "Newbie"]
#k = 3
#print(crazyball(players, k))

from itertools import product

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))        
    return sorted([int(s) for s in [''.join(str(z) for z in x) for x in product(createNumber(digits), repeat=k)] if int(s) % d==0])

digits = [1, 5, 2]
k = 2
d = 3
print(crackingPassword(digits, k, d))


