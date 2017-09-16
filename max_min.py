largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == 'done' : break
    try:
        number = float(num)
        if largest is None: largest = number
        if smallest is None: smallest = number
        
        if number>largest : largest = number
        if number<smallest : smallest = number
    except:
        print('invalid number, try again ...')
        continue
    print(num)

print('Maximum', largest)
print('Minimus', smallest)