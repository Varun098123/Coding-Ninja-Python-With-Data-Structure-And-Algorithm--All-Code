## Read input as specified in the question
## Print the required output in given format
N=int(input())
i=1
while(i<=N):
    j=1
    l=i
    while(j<=i):
        charP=chr(ord('A')+l-1)
        print(charP,end="")
        l=l+1
        j=j+1
    print()
    i=i+1