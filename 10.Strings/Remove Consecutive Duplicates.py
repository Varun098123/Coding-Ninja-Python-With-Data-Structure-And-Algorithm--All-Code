
from sys import stdin

def removeConsecutiveDuplicates(string) :
    str_len=len(string)
    i=0
    str=string[0]
    while i<str_len-1:
        if string[i]==string[i+1]:
            i=i+1
            # str+=
        else:
           i=i+1
           str+=string[i]
    return str


	


#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)