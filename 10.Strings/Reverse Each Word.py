
from sys import stdin


def reverseEachWord(string) :
	# Your code goes here
	words=string.split(" ")
	new=[]
	for word in words:
		new.append(word[::-1])
	str=" ".join(new)
	return str



#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)