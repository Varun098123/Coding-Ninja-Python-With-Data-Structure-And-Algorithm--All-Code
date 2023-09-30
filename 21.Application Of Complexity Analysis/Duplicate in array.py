import sys

def duplicateNumber(arr,n):
    # Please add your code here
    l=len(arr)
    s=0
    for i in range(0,l-1):
        s ^=i
        s ^=arr[i]
    return s^arr[l-1]


def takeInput() :
    n = int(sys.stdin.readline().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split()))
    return arr, n


t = int(sys.stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(duplicateNumber(arr, n))

    t -= 1