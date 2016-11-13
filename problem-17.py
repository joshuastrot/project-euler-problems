#!/usr/bin/env python

#Lists of all word combinations.
singleNumbers = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tenNumbers = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tenthNumbers = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
extraNumbers = ["hundred"]

#Start sequence of loops to generate combinations.
totalCount = 0

#Kept purely for debugging purposes.
numArray = []

#Loop for 1-9
for num in singleNumbers:
    totalCount = totalCount + len(num)
    numArray.append(num)

#Loop for 10-19
for num in tenNumbers:
    totalCount = totalCount + len(num)
    numArray.append(num)

#Loop for 20-99
for num in tenthNumbers:
    for sinNum in singleNumbers:
        totalCount = totalCount + len(num) + len(sinNum)
        numArray.append(num + sinNum)
    
#Loop for numbers 100-999
for num in extraNumbers:
    for sinNumHundreth in singleNumbers[1:]:
        totalCount = totalCount + len(sinNumHundreth) + len(num)
        numArray.append(sinNumHundreth + " " + num)

    for sinNumHundreth in singleNumbers[1:]:
        for sinNumFirst in singleNumbers[1:]:
            totalCount = totalCount + len(sinNumHundreth) + len(num) + len("and") + len(sinNumFirst)
            numArray.append(sinNumHundreth + " " + num + " and " + sinNumFirst)
            
    for sinNumHundreth in singleNumbers[1:]:
        for sinNumTenth in tenNumbers:
            totalCount = totalCount + len(sinNumHundreth) + len(num) + len("and") + len(sinNumTenth)
            numArray.append(sinNumHundreth + " " + num + " and " + sinNumTenth)
    
    for sinNumHundreth in singleNumbers[1:]:
        for tenthNum in tenthNumbers:
            for sinNum in singleNumbers:
                totalCount = totalCount + len(sinNumHundreth) + len(num) + len("and") + len(tenthNum) + len(sinNum)
                numArray.append(sinNumHundreth + " " + num + " and " + tenthNum + " " + sinNum)
    

#Print out final count.
totalCount = totalCount + len("onethousand")       
print totalCount