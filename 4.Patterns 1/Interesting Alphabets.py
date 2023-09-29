from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
N=int(input())
i=1
l=i
while(i<=N):
    j=1
    charP=chr(ord('A')+N-l)
    charP1=charP
    k=i
    while(j<=i):
        charP1=chr(ord('A')+N-k)
        print(charP1,end="")
        k=k-1
        j=j+1
    print()
    l=l-1
    i=i+1

