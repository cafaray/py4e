import re

requests= ["I need a new window.", 
 "I really, really want to replace my window!", 
 "Replace my window.", 
 "I want a new window.", 
 "I want a new carpet, I want a new carpet, I want a new carpet.", 
 "Replace my carpet"]
ids= [374, 2845, 83, 1848, 1837, 1500]
threshold = 0.5

def spamClusterization(requests, ids, threshold):
    sets = list()
    for e in requests:        
        words = re.findall('[a-z]+', e.lower())
        sets.append(set(words))
    ji = [[jaccardIndices(set1, set2) for set1 in sets] for set2 in sets] 
    
    #cluster = [ids[x] for x in range(0, len(ji)) if threshold in ji[x]]
    clusters = calculateSecond(threshold, ji, ids)
    print(clusters)
    #result = list()
    #if len(clusters) > 0:
    #    result.append(sorted(clusters))
    #if len(cluster2) > 0:
    #    result.append(sorted(clusters))
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

    result.append(sorted(cluster.get(threshold)))
    for item in clusters.items():
        if len(item[1]) > 0:
            result.append(sorted(item[1]))
    return result

print(spamClusterization(requests, ids, threshold))