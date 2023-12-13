class node:
    def __init__(self,data):
        self.data = data
        self.next = None 

def inputtolist():
    list = [int(x) for x in input().split()]
    head = None
    tail = None
    for x in list:
        if x == -1:
            break
        newnode = node(x)
        if head is None:
            head = newnode
            tail = newnode
        else:
            tail.next = newnode
            tail = newnode 
    return head

def printL(head):
    
    if head is None:
        return 
    while head is not None:
        print(str(head.data)+ "-->", end=" ")   
        
        head = head.next
    print(None)
    return

def count(head):
    c = 0
    while head is not None:
        c = c + 1
        head = head.next
    return c

def reverse(head):
    prev = None
    Next = None
    curr = head
    if head is None:
        return
    while curr is not None:
        Next = curr.next
        curr.next = prev
        prev = curr
        curr = Next 
    head = prev 
    return head 

def insert(head,i,data):
    if i < 0 or i > count(head):
        return 
    prev = None
    tail = head
    new = node(data)

    if i == 0:
        new.next = head
        head = new
        return head

    
    while i > 0:
        prev = tail
        tail = tail.next
        i = i - 1
    prev.next = new
    new.next = tail
    return head 
    
    
def delete(head,i):
    prev = None
    tail = head
    if i < 0 or i >= count(head):
        return head
    c = 0
    while c < i:
        prev = tail
        tail = tail.next
        c = c + 1
    if prev is not None: 
        prev.next = tail.next
    else:
        head = head.next
    return head
    

a = inputtolist()
printL(a)
b = delete(a,0)
printL(b)
#count(a)
#b = reverse(a)
#printL(b)


