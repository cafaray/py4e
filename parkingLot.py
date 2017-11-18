carDimensions = [4, 1]
parkingLot= [
 [1,0,1,0,1,0], 
 [1,0,0,0,1,0], 
 [0,0,0,0,0,1], 
 [1,0,0,0,1,1]]
luckySpot = [0, 3, 3, 3]

def printLote(parkingLot):
    print('--------------------------------------------------------------------------------')
    for y in range(0, len(parkingLot)):    
        print(parkingLot[y])
    print('--------------------------------------------------------------------------------')

def parkingSpot(carDimensions, parkingLot, luckySpot):
    A = luckySpot[0],luckySpot[1]
    B = luckySpot[0],luckySpot[3]
    C = luckySpot[2],luckySpot[1]
    D = luckySpot[2],luckySpot[3]
    print(A, B, C, D)
    available = 0

    for y in range(A[0], C[0]+1):
        for x in range(A[1], D[1]+1):
            #parkingLot[y][x] = 'X'
            if parkingLot[y][x] != 0:
                return False # el bloque esta ocupado
    #el lote esta desocupado, ahora veamos si inicia en las orillas, de ser así, esta libre:
    if luckySpot[1] == 0 or luckySpot[0] == 0:
        return True # el bloque es valido y esta al inicio/arriba del bloque so ...
    if luckySpot[3] == len(parkingLot[0])-1 or luckySpot[2] == len(parkingLot)-1:
        return True # el bloque es valido e inicia al final/abajo del bloque so ...
    
    bloqueado = False
    # validar que no existan obstaculos antes del lugar preferido, con la primera libre de obstaculos nos vamos:
    for y in range(A[0], C[0]): # itera las lineas del preferido
        for x in range(0, A[1]): # iteras las posiciones antes de iniciar el preferido
            if parkingLot[y][x] == 1:
                bloqueado = True
                break
        if bloqueado is True: break
    
    if bloqueado is False: return True # si no esta bloqueado entonces listo ...

    bloqueado = False # supondremos que no esta bloqueado
    for y in range(A[0], C[0]): # itera las lineas del preferido
        for x in range(len(parkingLot[0]) - 1, B[1], -1): # iteras las posiciones del fin al termino del preferido
            if parkingLot[y][x] == 1:
                bloqueado = True
                break
        if bloqueado is True: break
    
    if bloqueado is False: return True # si no esta bloqueado entonces listo ...

    bloqueado = False # supondremos que no esta bloqueado
    for y in range(0, A[0]): # itera las lineas de arriba hacia el inicio del preferido
        for x in range(A[1], B[1]): # iteras las posiciones de inicio a fin del preferido
            if parkingLot[y][x] == 1:
                bloqueado = True
                break
        if bloqueado is True: break
    
    if bloqueado is False: return True # si no esta bloqueado entonces listo ...

    bloqueado = False # supondremos que no esta bloqueado
    for y in range(len(parkingLot)-1, C[0], -1): # itera las lineas de abajo hacia el final del preferido
        for x in range(C[1], D[1]): # iteras las posiciones de inicio a fin del preferido
            if parkingLot[y][x] == 1:
                bloqueado = True
                break
        if bloqueado is True: break
    
    if bloqueado is False: return True # si no esta bloqueado entonces listo ...    
    return False

res = parkingSpot(carDimensions,parkingLot,luckySpot)
print(res)
