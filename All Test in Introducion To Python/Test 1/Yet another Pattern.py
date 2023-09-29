from os import *
from sys import *
from collections import *
from math import *

def ninjaPuzzle(n):


    # Write your Code and
    # Print the output Pattern here only.
    i=1
    while(i<=n):
        spaces=1
        while(spaces<=i-1):
            print(" ",end="")
            spaces=spaces+1
        j=1
        while(j<=n-i+1):
           print("*",end="")
           j=j+1
        print()
        i=i+1



