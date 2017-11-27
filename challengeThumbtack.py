import re

requests= ["I need a new window"]
ids= [239]
threshold = 0

def spamClusterization(requests, ids, threshold):
    sets = list()
    for e in requests:        
        words = re.findall('[a-z]+', e.lower())
        sets.append(set(words))
    ji = [[jaccardIndices(set1, set2) for set1 in sets] for set2 in sets] 
    clusters = calculateSecond(threshold, ji, ids)    
    return clusters
    
def jaccardIndices(set1, set2):    
    return round(len(set1.intersection(set2)) / float(len(set1.union(set2))), 2)

def calculateSecond(threshold, sets, ids):
    result = list()
    cluster = dict() 
    clusters = dict()
    for x in range(0, len(sets)):
        for y in range(0, len(sets[x])):
            if x!=y:
                key = sets[x][y]
                if key == threshold:
                    if cluster.get(key):
                        if ids[x] not in cluster[key]:                        
                            cluster[key].append(ids[x])
                    else:
                        cluster[key] = [ids[x], ids[y]]
                elif key > threshold:
                    if clusters.get(key):
                        if ids[x] not in clusters[key]:                        
                            clusters[key].append(ids[x])
                    else:
                        clusters[key] = [ids[x], ids[y]]
    if cluster.get(threshold):
        result.append(sorted(cluster.get(threshold)))
    for item in clusters.items():
        if len(item[1]) > 0:
            result.append(sorted(item[1]))
    return result

print(spamClusterization(requests, ids, threshold))