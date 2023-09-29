from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
i=1
while(i<=N):
    spaces=1
    while(spaces<=N-i):
        print(" ",end="")
        spaces=spaces+1
    p=i # for increasing
    j=1
    while(j<=i):
        print(p,end="")
        p=p+1
        j=j+1
    
    p=p-2 # from that moment it wil be decreases to i
    while(p>=i):
        print(p,end="")
        p=p-1
    print()
    i=i+1