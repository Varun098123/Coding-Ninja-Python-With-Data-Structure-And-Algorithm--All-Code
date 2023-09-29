## Read input as specified in the question
N=int(input())
i=1
while(i<=N):
    spaces=1
    while(spaces<=N-i):
        print(" ",end="")
        spaces=spaces+1
    number=1
    while(number<=i):
        print(number,end="")
        number=number+1
    print()
    i=i+1