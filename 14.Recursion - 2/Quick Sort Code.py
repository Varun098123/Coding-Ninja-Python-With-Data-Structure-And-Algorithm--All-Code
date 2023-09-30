"""
	The function is called with the parameters:
	quickSort(input, 0, size - 1);

"""


def partition(a,si,ei):
    # Write your code here
    pivot = a[si]
    
    count = 0
    for i in range(si,ei+1):
        
        if a[i] < pivot:
            count+=1
    
    a[si+count],a[si] = a[si],a[si+count]
    pivot_index = si+count
    
    i = si
    j = ei
    
    while i < j:  #pivot ko deno point karenge if i==j
        
        if a[i]<pivot:
            i+=1
        
        elif a[j] >= pivot:
            j-=1
        
        else:
            a[i],a[j] = a[j],a[i]
            i+=1
            j-=1
            
    return pivot_index
    


def quickSort(a, si, ei):
    """
    Don't write main().
    Don't read input, it is passed as function argument.
    Change in the given array itself.
    Taking input and printing output is handled automatically.
    """
    if si > ei:
        return 
    
    pivot_index = partition(a,si,ei)
    quickSort(a,si,pivot_index-1)
    quickSort(a,pivot_index+1,ei)
    

