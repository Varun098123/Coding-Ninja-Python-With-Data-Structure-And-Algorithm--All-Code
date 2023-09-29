def search(nums: [int], target: int):
    # Your code goes here
    l=0
    u=len(nums)-1
    while(l<=u):
        mid=(l+u)//2
        if(nums[mid]==target):
            return mid
        elif(target>nums[mid]):
            l=mid+1
        else:
            u=mid-1
    
    return -1
