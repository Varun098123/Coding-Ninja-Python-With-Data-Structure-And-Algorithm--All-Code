# Problem: Remove x from string
def removeX(string): 
    chr="x"
    if(len(string)==0):
        return string
    smallerOutput=removeX(string[1:])
    if(string[0]==chr):
        return ""+smallerOutput
    else:
        return string[0]+smallerOutput


# Main
string = input()
print(removeX(string))
