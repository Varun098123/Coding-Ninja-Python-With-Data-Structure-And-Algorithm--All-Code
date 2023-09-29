#Write Your Code Here
N=int(input())
rev=0
while(N>0):
    digit=N%10
    rev=rev*10+digit
    N=N//10
print(rev)
