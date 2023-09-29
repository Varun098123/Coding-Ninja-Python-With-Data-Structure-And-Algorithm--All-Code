# Read input as sepcified in the question
# Print output as specified in the question

S=int(input())
E=int(input())
W=int(input())
for f in range(S,E+1,W):
    c=int((f-32)*(5/9))
    print(f,"",c)