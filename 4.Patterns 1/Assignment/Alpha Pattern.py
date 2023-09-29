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
    charP=chr(ord('A')+i-1)
    while(j<=i):
        print(charP,end="")
        j=j+1
    print()
    i=i+1
