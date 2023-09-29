from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
i=1
while(i<=N):
    spaces=1 #for spaces
    while(spaces<=N-i):
        print(" ",end="")
        spaces=spaces+1
    j=i #for increasing
    while(j>0):
        print(j,end="")
        j=j-1
    j=2 #for increasing
    while(j<=i):
        print(j,end="")
        j=j+1
    print()
    i=i+1
