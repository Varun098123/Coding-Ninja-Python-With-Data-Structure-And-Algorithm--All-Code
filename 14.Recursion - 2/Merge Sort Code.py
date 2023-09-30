def merge(left, right, arr):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1
    
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1




    
def mergeSort(arr,si,ei):
    if len(arr) == 0 or len(arr) == 1:
        return 
    mid = len(arr)//2
    a1 = arr[0:mid]
    si=0
    ei=len(a1)-1
    mergeSort(a1,si,ei)
    a2 = arr[mid:]
    si=0
    ei=len(a2)-1
    mergeSort(a2,si,ei)
    merge(a1,a2,arr)

# Main
# n = int(input())
# arr = [int(i) for i in input().strip().split(' ')]
# mergeSort(arr)
# print(*arr)