## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
N=int(input())
evenSum=0
oddSum=0
while(N>0):
    digit=N%10
    if(digit % 2==0):
        evenSum=evenSum+digit
    else:
        oddSum=oddSum+digit
    N=N//10

print(evenSum,"",oddSum)
