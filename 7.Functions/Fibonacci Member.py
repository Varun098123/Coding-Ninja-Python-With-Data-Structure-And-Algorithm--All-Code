import math 
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
def isFibonacci(n): 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

n=int(input())
if (isFibonacci(n)==True):
    print("true")
else:
    print("false")