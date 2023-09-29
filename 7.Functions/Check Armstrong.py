from os import *
from sys import *
from collections import *
from math import *
n=int(input())
num=n
k=n
count=0
while(n>0):
    count=count+1
    n=n//10

sum=0
digit=0
while(num>0):
    digit=num%10
    sum=sum+(digit**count)
    num=num//10

if(k==sum):
    print("true")
else:
    print("false")