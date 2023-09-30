from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def stairCase(n):
    
    if n == 0 or n == 1:
        return 1
    
    elif n == 2:
        return  2
    
    else:
        return stairCase(n-1) + stairCase(n-2) + stairCase(n-3)
    
N=int(input())
print(stairCase(N))