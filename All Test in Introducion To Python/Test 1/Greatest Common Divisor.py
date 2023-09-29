from os import *
from sys import *
from collections import *
from math import *

def findGcd(x, y):
    # Write your code here
    # Return an integer

 
    # Everything divides 0
    if (x == 0):
        return y
    if (y == 0):
        return x
 
    # base case
    if (x == y):
        return x
 
    # a is greater
    if (x > y):
        return gcd(x-y, y)
    return gcd(x, y-x)
    