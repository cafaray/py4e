# 7.2 Write a program that prompts for a file name, 
# then opens that file and reads through the file, 
# looking for lines of the form:
#     X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values
# from each of the lines and compute the average of those
# values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name
fname = input('Enter file name: ')
try:
    fhandle = open(fname)

except:
    print('El archivo indicado no existe')
    quit()

fltSum = 0;
intCount = 0;
for line in fhandle:
    if not line.startswith('X-DSPAM-Confidence:') : continue
    intPosition = line.find(':')+1
    strNumber = line[intPosition:].strip()
    try:
        fltNumber = float(strNumber)
    except:
        print('wrong number:',strNumber)
        continue
    fltSum = fltSum + fltNumber
    intCount = intCount + 1
    # print(line)
fltAverage = fltSum / intCount
print('Average spam confidence:', fltAverage)

