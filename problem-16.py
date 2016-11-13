#!/usr/bin/env python

#Calculate value of 2^1000
value = 2**1000

#Generate list of all integers in value
lst = [int(i) for i in str(value)]

#Calculate sum
total = 0
for num in lst:
    total = total + num
    
print total