from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def lastIndex(a,x,si):
    l=len(a)
    if(si==l):
        return -1
    smallerListOutput=lastIndex(a,x,si+1)
    if(smallerListOutput != -1):
        return smallerListOutput
    else:
        if(a[si]==x):
            return si
        else:
            return -1

N=int(input())
a=[int(i) for i in input().split()]
x=int(input())
si=0
print(lastIndex(a,x,si))