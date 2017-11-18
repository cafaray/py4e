import math
departure= [0, 0.2]
destination= [7, 0.5]

def perfectCity(departure, destination):
    x1 = departure[0]
    y1 = departure[1]
    x2 = destination[0]
    y2 = destination[1]
    
    dx = 0
    if not (isinstance(x1, int) or isinstance(x2, int)):
#        if x2 > x1: # va a la derecha
        der = math.ceil(x1) - x1        
        if math.ceil(x1) > x2:
            der += math.ceil(x1) - x2
        else:
            der += x2 - math.ceil(x1)
#        else: # va a la izquierda
        izq = x1 - math.floor(x1)
        if math.floor(x1) > x2:
            izq += math.floor(x1) - x2
        else:
            izq += x2 - math.floor(x1)
        dx = min(der, izq)
    else:
        dx += abs(x2-x1)
    
    dy = 0
    if not (isinstance(y1, int) or isinstance(y2, int)):
        #if y2 > y1: # va hacia arriba
        arr = math.ceil(y1) - y1        
        if math.ceil(y1) > y2:
            arr += math.ceil(y1) - y2
        else:
            arr += y2 - math.ceil(y1)
        #else: # va hacia abajo
        aba = y1 - math.floor(y1)        
        if math.floor(y1) > y2:
            aba += math.floor(y1) - y2
        else:
            aba += y2 - math.floor(y1)
        dy = min(arr, aba)
    else:
        dy += abs(y2-y1)
    return dx + dy

print(perfectCity(departure, destination))

#from decimal import Decimal

#ride_time = 30
#ride_distance = 7
#cost_per_minute = [0.2, 0.35, 0.4, 0.45]
#cost_per_mile = [1.1, 1.8, 2.3, 3.5]

#def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
#    xtime = list(map(lambda x, y: round((x * ride_time) + (y*ride_distance),2), cost_per_minute, cost_per_mile))    
#    print(xtime)

#fareEstimator(ride_time,ride_distance,cost_per_minute, cost_per_mile)