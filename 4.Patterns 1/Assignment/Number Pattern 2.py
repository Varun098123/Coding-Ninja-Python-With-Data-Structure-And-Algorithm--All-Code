from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
i=1
print(1)
while i<=N-1:
    print(i,end="")
    num_2=2
    while num_2<=i: #no of Colums
        print("0",end="")
        num_2+=1
    print(i)
    i=i+1
