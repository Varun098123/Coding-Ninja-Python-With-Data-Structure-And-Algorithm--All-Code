## Write your code here
## To take space separated input for two variables, we use the following syntax (3 lines)
## a, b = input().split()
## a = int(a)
## b = int(b)
def power(x,n):
    if(n==0): #base case
        return 1
    return x*power(x,n-1)

x,n=input().split()
x=int(x)
n=int(n)
print(power(x,n))