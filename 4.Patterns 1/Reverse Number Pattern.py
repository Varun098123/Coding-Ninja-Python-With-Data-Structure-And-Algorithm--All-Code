## Read input as specified in the question
## Print the required output in given format
N=int(input())
i=1
while(i<=N):
    j=1
    k=i
    while(j<=i):
        print(k,end="")
        k=k-1
        j=j+1
    print()
    i=i+1