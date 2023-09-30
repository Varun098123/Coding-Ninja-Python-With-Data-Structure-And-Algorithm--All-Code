from sys import stdin

def merge(a1, a2, arr):
    i = 0
    j = 0
    index = 0
    
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            arr[index] = a1[i]
            i = i + 1
        else:
            arr[index] = a2[j]
            j = j + 1
            
        index = index + 1
        
    while i < len(a1):
        arr[index] = a1[i]
        i = i + 1
        index = index + 1
        
    while j < len(a2):
        arr[index] = a2[j]
        j = j + 1
        index = index + 1

def sort(arr):
    if len(arr) <= 1:
        return
    
    mid = len(arr) // 2
    a1 = arr[0 : mid]
    a2 = arr[mid : ]
    
    sort(a1)
    sort(a2)
    merge(a1, a2, arr)
        
def intersection(arr1, arr2, n, m) :
    sort(arr1)
    sort(arr2)
    
    i = 0
    j = 0
    
    while i < n and j < m:
        if arr1[i] == arr2[j]:
            print(arr1[i], end = ' ')
            i = i + 1
            j = j + 1
        elif arr1[i] < arr2[j]:
            i = i + 1
        else:
            j = j + 1

# Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
    	return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

#main
t = int(stdin.readline().strip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()
    intersection(arr1, arr2, n, m)
    print()

    t -= 1