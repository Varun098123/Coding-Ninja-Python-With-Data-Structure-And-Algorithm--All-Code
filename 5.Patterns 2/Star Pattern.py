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
    stars=1 #increase
    while(stars<=i):
        print("*",end="")
        stars=stars+1
    stars=i-1
    while(stars>=1):
        print("*",end="")
        stars=stars-1
    print()
    i=i+1