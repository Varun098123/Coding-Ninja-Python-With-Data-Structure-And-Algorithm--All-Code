from sys import stdin

def spiralPrint(mat, row, col):
    if row == 0:
        return
    
    rowStart, colStart = 0, 0

    numElements = row * col
    count = 0

    while count < numElements:
        i = colStart
        while i < col and count < numElements:
            print(mat[rowStart][i], end = " ")
            count += 1
            i += 1
        
        rowStart += 1

        i = rowStart
        while i < row and count < numElements:
            print(mat[i][col - 1], end = " ")
            count += 1
            i += 1
        
        col -= 1

        i = col - 1

        while i >= colStart and count < numElements:
            print(mat[row - 1][i], end = " ")
            count += 1
            i -= 1
        
        row -= 1

        i = row - 1
        while i >= rowStart and count < numElements:
            print(mat[i][colStart], end = " ")
            count += 1
            i -= 1
        
        colStart += 1


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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1