from os import *
from sys import *
from collections import *
from math import *

N=int(input())
i=1
j=N #this j for last loop
while(i<=N):
    p=1
    while(p<=N):
        if(p==i):
            print("*",end="")
        else:
            print("0",end="")
        p=p+1
    print("*",end="")
    p=1
    while(p<=N):
        if(p==j):
            print("*",end="")
        else:
            print("0",end="")
        p=p+1
    j=j-1
    print()
    i=i+1