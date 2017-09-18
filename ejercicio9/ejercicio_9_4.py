# Write a program to read through the mbox-short.txt 
# and figure out who has the sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word 
# of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps 
# the sender's mail address to a count of the number 
# of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary 
# using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhandler = open(name)
counts = dict()
for line in fhandler:
    if line.startswith('From '):
        words = line.split()
        account = words[1]
        counts[account] = counts.get(account, 0) + 1

maxCount = None
account = None
for k,v in counts.items():
    if maxCount is None: 
        maxCount = v
        account = k
    if v > maxCount: 
        maxCount = v
        account = k

print(account,maxCount)