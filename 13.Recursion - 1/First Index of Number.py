def firstIndex(arr, x,si):
    # Please add your code here
    l=len(arr)
    if(si==l):
        return -1
    if(arr[si] == x):
        return si
    next=firstIndex(arr,x,si+1)
    return next

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
si=0
print(firstIndex(arr, x,si))
