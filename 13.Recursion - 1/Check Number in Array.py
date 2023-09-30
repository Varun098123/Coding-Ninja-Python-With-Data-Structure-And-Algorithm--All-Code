def checkNumber(arr, x,n):
    # Please add your code here
    if(n==0):
        return False
    if(arr[n-1]==x):
        return True
    else:
        return checkNumber(arr,x,n-1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
n=len(arr)
if checkNumber(arr, x,n):
    print('true')
else:
    print('false')
