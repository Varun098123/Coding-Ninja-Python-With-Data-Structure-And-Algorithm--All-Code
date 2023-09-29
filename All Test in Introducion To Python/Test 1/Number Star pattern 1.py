from os import *
from sys import *
from collections import *
from math import *
N=int(input())
i=1
while(i<=N):
    j=N
    while(j>0):
        if(j!=i):
            print(j,end="")
        else:
            print("*",end="") 
        j=j-1
    print()
    i=i+1
    