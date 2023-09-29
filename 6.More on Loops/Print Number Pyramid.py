from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
i=1
while(i<=N-1):
    spaces=1
    while(spaces<=i-1):
        print(" ",end="")
        spaces=spaces+1
    j=i
    while(j<=N):
        print(j,end="")
        j=j+1
    spaces=1    
    print()
    i=i+1


i=1
while(i<=N):
    spaces=1
    while(spaces<=N-i):
        print(" ",end="")
        spaces=spaces+1
    p=N-i+1
    while(p<=N):
        print(p,end="")
        p=p+1
    print()
    i=i+1

# Output
# 6
# 123456
#  23456
#   3456
#    456
#     56
#      6
#     56
#    456
#   3456
#  23456
# 123456

