# These are the full solutions for Homework 1 in AMATH 301, Winter 2023 

import numpy as np
import matplotlib.pyplot as plt

######### Problem 1 ##########
# Use a for loop!
temp = np.arange(32)
for k in range(32):
    k = k + 1
    temp[k-1] = k*(k + 1)*(2*k + 1)/6
A1 = temp

######### Problem 2 ##########
## Part a
# I will start this off for you, you will need to finish it.
y1 = 0 # We will start off with y1 = 0 and then add to it.
term = 0.1
for k in range(100_000):
    y1 = y1 + term
A2 = y1

y2 = 0
term = 0.1
for k in range(100_000_000):
    y2 = y2 + term
A3 = y2

y3 = 0
term = 0.25
for k in range(100_000_000):
    y3 = y3 + term
A4 = y3

y4 = 0
term = 0.5
for k in range(100_000_000):
    y4 = y4 + term
A5 = y4
## Part b - Now take the difference, don't forget absolute value!
x1 = np.abs(10_000 - y1)
A6 = x1

x2 = np.abs(y2 - 10_000_000)
A7 = x2

x3 = np.abs(25_000_000 - y3)
A8 = x3

x4 = np.abs(y4 - 50_000_000)
A9 = x4

######### Problem 3 ##########
Fibonacci = np.empty(200)

Fibonacci[0] = 1
Fibonacci[1] = 1

## Part c
temp = 0
for i in range(2, 200, 1):
    if(Fibonacci[i-1] + Fibonacci[i-2] >= 1_000_000):
        n = i - 1
        break
    Fibonacci[i] = Fibonacci[i-1] + Fibonacci[i-2]
A10 = Fibonacci
A11 = n

A12 = Fibonacci[:n+1]

print(A10)
print()
print(A11)
print(A12)
## Part e
# Slice! If N is the variable corresponding to the k you found above, then
# slice up through (including) N.


######### Problem 4 ##########
## Part a
# I will let you create x here.

## Part b
# Assuming that x is defined correctly above, now we can just do regular
# arithmetic with it. Compare to what you did in Problem 2.
# Taylor = 0*x # Initialize the Taylor approximation - Remove this once you
                # define x!
# for loop here
# update Taylor in the for loop using the formula in the sum!
