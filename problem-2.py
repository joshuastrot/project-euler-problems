# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

#Upper Threshold
quantity = 4000000

#Calculate fibs, adding all even ones. Using binet's formula.
x = 0
fib = 0
fibTotal = 0
while fib < quantity:
    fib = int((( 1 + sqrt(5) )**x - ( 1 - sqrt(5) )**x ) / (2**x * sqrt(5)))
    
    if fib % 2 == 0:
        fibTotal = fibTotal + fib
    
    x = x + 1

print fibTotal