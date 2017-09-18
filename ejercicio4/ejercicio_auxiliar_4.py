def suma(val1, val2):
    try:
        suma = int(val1) + int(val2)
        return suma
    except:
        print('Algo ha ocurrido que no logramos hacer la suma')

x = input('Coloca un numero: ')
y = input('Dame otro numero: ')

print(suma(x, y))
