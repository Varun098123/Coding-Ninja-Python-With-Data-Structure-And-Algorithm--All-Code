from sys import stdin

def arrayEquilibriumIndex(arr, n) :
    #Your code goes here
    ts=0 #ts=total sum
    i=0
    while(i<n):
        ts=ts+arr[i]
        i=i+1

    ls=0 #ls=left sum
    i=0
    while(i<n):
        rs=ts-ls-arr[i] #rs=right sum
        if(ls==rs):
            return i
            
        ls=ls+arr[i]
        i=i+1
    else:
        return -1


#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t-= 1