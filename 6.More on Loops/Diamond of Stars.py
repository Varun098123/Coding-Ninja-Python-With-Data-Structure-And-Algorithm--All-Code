from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
N=(N//2)+1
i=1
while(i<=N):
    spaces=1
    while(spaces<=N-i):
        print(" ",end="")
        spaces=spaces+1
    j=1
    while(j<=(2*i)-1):
        print("*",end="")
        j=j+1
    print()
    i=i+1

i=1
while(i<=N-1):
    spaces=1
    while(spaces<=i):
        print(" ",end="")
        spaces=spaces+1
    star=1 #for increasing
    while(star<=N-i):
       print("*",end="")
       star=star+1
    
    star=star-1 #for decreasing
    while(star>=2):
        print("*",end="")
        star=star-1
    print()
    i=i+1

# Output
# 5
#   *
#  ***
# *****
#  ***
#   *
