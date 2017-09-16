# Regular expressions
# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.

import re

name = input("Enter file:")
if len(name) < 1 : name = "actual-data.txt"

try:
    fhandle = open(name)
except:
    print('File does not exist')
    quit()

numbers = list()
for line in fhandle:
    numbers = numbers + re.findall("[0-9]+", line)
#print(numbers)

iNumbers = list()
for number in numbers:
    iNumbers.append(int(number))

print(sum(iNumbers))


