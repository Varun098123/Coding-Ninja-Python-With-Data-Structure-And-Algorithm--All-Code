from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def printStar(s):
    if(len(s)==0 or len(s)==1): #base case
        return s
    if(s[0]==s[1]):
        return s[0]+"*"+printStar(s[1:])
    else:
        return s[0]+printStar(s[1:])
    
s=input()
print(printStar(s))