from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def geometric(k):
    if(k==0):
        return 1
    smallerOutput=geometric(k-1)
    return ((1/2)**k)+smallerOutput

k=int(input())
ans=geometric(k)
print("%.5f"%ans)
