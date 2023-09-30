'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def length(head) :
    #Your code goes here
    count=0
    temp=head
    while temp is not None:
        count=count+1
        temp=temp.next
    return count