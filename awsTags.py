def subStringsKDist(inputStr, num):
    # WRITE YOUR CODE HERE
    words = dict()
    idx = 0
    for idx in range(0, len(inputStr) - num + 1):
        newstr = inputStr[idx:idx+num]
        prospect = True
        for i in range(0, num-1):
            c = newstr[i]
            if c in newstr[i+1:]:
                prospect = False
                break
            else:
                continue
        if prospect == True:
            words[newstr] = words.get(newstr, 0) + 1 
    return list(words.keys())


inputStr = "awaglknagawunagwkwagl"
#inputStr = "abcd"
num = 4

print(subStringsKDist(inputStr, num))



def subSequenceTags(targetList, availableTagList):
    #tags = dict()
    #lst = list()
    for x in targetList:
        try:
            nomatter = availableTagList.index(x)
        except:
            return [0]
    resta = 0
    lastResta = len(availableTagList)
    first = -1
    last = -1
    for x in range(0, len(availableTagList)):
        try:
            idxmin = len(availableTagList) - x
            idxmax = 0;
            for target in targetList:
                idx = availableTagList.index(target, x) 
                if idx < idxmin:
                    idxmin = idx 
                if idx > idxmax:
                    idxmax = idx
            #lst.append(availableTagList[idxmin:])
            print(idxmin, idxmax)
            resta = idxmax - idxmin
            if resta < lastResta:
                lastResta = resta
                first = idxmin
                last = idxmax
        except:
            continue

    #for s in lst:
    #    print(s)
    return [first, last]

    

targetList = ["in", "the", "spain"]
availableTagList = ["the", "spain", "that", "the", "rain", "in", "spain","stays","forecast","in", "the"]
print(subSequenceTags(targetList, availableTagList))





















