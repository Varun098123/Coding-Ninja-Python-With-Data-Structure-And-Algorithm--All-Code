from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
i=1
k=1#we have to print only 1 therefore k=1 
while(i<=N):
    j=1
    while(j<=i):
        print(k,end="")
        j=j+1
    print()
    i=i+1
