
from sys import stdin


def isPermutation(string1, string2) :
	#Your code goes here
    ans=False
    if(len(string1) == len(string2) ):
        if(sorted(string1) == sorted(string2)):
           return True
        else:
           return ans
    else:
        return ans


#main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

