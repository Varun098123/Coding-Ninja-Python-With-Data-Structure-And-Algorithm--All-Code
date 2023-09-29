# Write your code here
while True:
    i = int(input())
    if(i == 1):
        a = int(input())
        b = int(input())
        c = a+b
        print(c)
    elif(i == 2):
        a = int(input())
        b = int(input())
        c = a-b
        print(c)
    elif(i == 3):
        a = int(input())
        b = int(input())
        c = a*b
        print(c)
    elif(i == 4):
        a = int(input())
        b = int(input())
        c = a/b
        print(int(c))
    elif(i == 5):
        a = int(input())
        b = int(input())
        c = a%b
        print(int(c))
    elif(i == 6):
        quit()
    else:
        print("Invalid Operation")