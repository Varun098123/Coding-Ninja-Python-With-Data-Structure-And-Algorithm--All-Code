def bubbleSort(arr: [int], size: int):
    # Your code goes here.
    for i in range(size):
        for j in range(size-1):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j] #swap