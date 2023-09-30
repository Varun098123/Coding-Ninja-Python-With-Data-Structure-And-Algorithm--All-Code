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
    if(n%10==0):
        return 1+digit
    else:
        return digit
N=input()
n=int(N)
if(n==0):
    print(1)
else:
    print(sum(n))


# Output
# 11
