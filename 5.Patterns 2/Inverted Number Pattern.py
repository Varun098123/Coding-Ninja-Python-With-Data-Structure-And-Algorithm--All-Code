## Read input as specified in the question
## Print the required output in given format
N=int(input())
i=1
k=N
while(i<=N):
    j=1
    while(j<=N-i+1):
        print(k,end="")
        j=j+1
    print()
    k=k-1
    i=i+1