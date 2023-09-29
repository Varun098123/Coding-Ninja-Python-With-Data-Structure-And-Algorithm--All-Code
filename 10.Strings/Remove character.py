
from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here
	li=list(string)
	new=[]
	for i in range(len(li)):
		if(li[i] != ch):
			new.append(li[i])
	string="".join(new)
	return string


#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)