n=int(input())
i=1
while(i<=n):
    num=1 #for increasing
    while(num<=i):
        print(num,end="")
        num=num+1
    spaces=1 #for spaces
    while(spaces<=((n-i)*2)): #imp step for spacing
        print(" ",end="")
        spaces=spaces+1
    num=i #for decreasing
    while(num>0):
        print(num,end="")
        num=num-1
    print()
    i=i+1
