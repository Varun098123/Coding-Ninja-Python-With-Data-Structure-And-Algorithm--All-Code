from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
i=1
while(i<=N):
    j=1
    while(j<=N-i+1):
        if(i%2==0):# 0 is printed on even ith row
            print(0,end="")
        else:# 1 is printed on odd ith row
            print(1,end="")
        j=j+1
    print()
    i=i+1