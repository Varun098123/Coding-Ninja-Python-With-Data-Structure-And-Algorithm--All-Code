from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
i=1
k=1
print_1=1
print_2=2
while(i<=N):
    j=1
    l=1
    while(j<=i):
        if(k==i and l==1):
            print(print_1,end="")
        elif(k==i and i-j==0):
            print(print_1,end="")
        else:
            print(print_2,end="")
        l=l+1
        j=j+1
    print()
    k=k+1
    i=i+1