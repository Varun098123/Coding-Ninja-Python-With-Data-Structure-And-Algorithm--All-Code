from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def sum(n):
    if(n<=0.0):
        return 0
    digit=sum(n//10)
    return int(n%10) + digit

N=int(input())
print(sum(N))