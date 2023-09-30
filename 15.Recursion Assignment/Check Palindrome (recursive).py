from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def reverse(S,n):
    if(n==-1):
        return ""
    smallOutput=reverse(S,n-1)
    return S[n]+smallOutput
S=input()
n=len(S)-1
s=reverse(S,n)
if(s==S):
    print("true")
else:
    print("false")
