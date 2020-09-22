import re
from collections import Counter

file1 = open("mbox.txt","r+")
FromEmailList = re.findall ('From: \S+@\S+', file1.read())
FromEmailList = [s.strip('From: ') for s in FromEmailList]
C = Counter(FromEmailList)

newArrayList = [ [k,]*v for k,v in C.items()]
lengthFromArray = []
print('Email with count')
for element in newArrayList:
    print(element[0], len(element))
    lengthFromArray.append(len(element))

maxNumber = max(lengthFromArray)

print('--------------------------------------------------------------------')
for element in newArrayList:
    if(maxNumber == len(element)):
        print('Max Email with count', element[0], len(element))