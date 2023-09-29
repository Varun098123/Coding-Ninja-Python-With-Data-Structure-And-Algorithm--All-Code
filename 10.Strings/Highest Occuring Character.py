def highestOccuringChar(string) :
    a = [0] * 256
    for i in string:
        x = ord(i)
        a[x] += 1
    max = 0
    ans = ""
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
            ans = chr(i)
    return ans

string = input()
ans = highestOccuringChar(string)

print(ans)