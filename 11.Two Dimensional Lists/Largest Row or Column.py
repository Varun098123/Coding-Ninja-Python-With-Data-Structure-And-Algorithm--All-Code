from sys import stdin
MIN_VALUE=-2147483648
def findLargest(arr, nRows, mCols):
    isRow=True
    largestSum=MIN_VALUE
    num=0
   
    for i in range(nRows):
        row_sum=0
        for j in range(mCols):
            row_sum+=arr[i][j]
        if row_sum > largestSum:
                largestSum=row_sum
                num=i
    
    for j in range(mCols):
        col_sum=0
        
        for i in range(nRows):
            col_sum=col_sum+arr[i][j]
        if col_sum > largestSum:
            largestSum=col_sum
            num=j
            isRow=False
    if isRow:
        print("row " + str(num) + " " +str(largestSum))
    else:
        print("column " + str(num) + " " +str(largestSum))
            
    #Your code goes here


#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1