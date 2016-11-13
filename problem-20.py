#!/usr/bin/env python

#Initial product
product = 1

#Generate 100 factorial
for x in range(1, 101):
    product = product * x

#Sum the digits of 100 factorial. Convert to string so product is iterable.
sum = 0   
for l in str(product):
    sum = sum + int(l)
    
print sum