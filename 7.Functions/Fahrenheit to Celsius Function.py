def printTable(start,end,step):
#Implement Your Code Here
    while(start<=end):
        c=int((start-32)*(5/9))
        print(start,c)
        start=start+step

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)

#c=(f-32)*(5/9)





