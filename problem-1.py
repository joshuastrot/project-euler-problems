#!/usr/bin/env python

#Generate list of multiples of three
x = 1
y = 1
multiplesThree = []
while x < 999:
    x = y * 3
    y = y + 1
    multiplesThree.append(x)

#Generate list of multiples of five. Don't add those which are already in set 3
x = 1
y = 1
multiplesFive = []
while x < 995:
    x = y * 5
    y = y + 1
    if x % 3 != 0:
        multiplesFive.append(x)
       

#Sum all of the multiples.
total = 0
for multiple in (multiplesFive + multiplesThree):
    total = total + multiple
    
print total