from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)


def getCompressedString(string) :
	# Write your code here.
    i=0
    new=''
    while(i<len(string)):
        j=i+1
        count=1
        while j<len(string) and (string[i]==string[j]):
            j+=1
            count+=1
        if count==1:
            new+=string[i]
        else:
            new+=string[i]+str(count)
        i=j
    return new

# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)