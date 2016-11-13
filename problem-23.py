#!/usr/bin/env python

#Function to factor numbers. 
#Takes an int value and returns a list of factors.
def factor(factorValue):
    factors = []
    valueFactoring = 1
    
    while valueFactoring <= (factorValue / 2):
        if factorValue % valueFactoring is 0:
            factors.append(valueFactoring)
            
        valueFactoring += 1
        
    return factors

#List to be populated with abundent numbers.
abundantNumbers = []

#Loop to identify all abundant numbers.
for num in range(11, 28124):
    numFactors = factor(num)
    if num < sum(numFactors):
        abundantNumbers.append(num)

#Uncomment this line to display list of abundant numbers.
#print sorted(abundantNumbers) 

#Populate a list of all the abundant sums. Will contain duplicates, but they will be removed in conversion to set.
abundantSums = []
for numOne in abundantNumbers:
    for numTwo in abundantNumbers:
        abundantSums.append(numOne + numTwo)

#Return the list of the abundant sums
print sum(list(set(range(1, 28124)) - set(abundantSums)))