from sys import stdin

# Following is the Node class already written for the Linked List.
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def length(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    return count

def deleteNode(head, pos) :
    # Write your code here.
    if(pos <0 or pos > length(head) or pos>length(head)-1):
        return head
    count=0
    curr=head
    prev=None
    while(count<pos):
        prev=curr
        curr=curr.next
        count=count+1
    if prev is not None:
        prev.next=curr.next
    else:
        head=head.next
    return head
    

























# Taking Input Using Fast I/O.
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head



# To print the linked list.
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


# Main.
t = int(stdin.readline().strip())

while t > 0 :
    
    head = takeInput()
    pos = int(stdin.readline().rstrip())
    
    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1
