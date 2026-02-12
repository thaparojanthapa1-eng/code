class singlynode:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next
    
    def __str__(self):
        return str(self.val)
    
Head=singlynode(1)
A=singlynode(2)
B=singlynode(3)
C=singlynode(4)

Head.next=A
A.next=B
B.next=C

# #treversing a linked list
curr=Head
while curr:
    print(curr)
    curr=curr.next

#display linked list - O(n) complexity
def display(Head):
    curr=Head
    elements=[]
    while curr:
        elements.append(str(curr.val))
        curr=curr.next
    print(" -> ".join(elements))

display(Head)

#search for value - O(n) complexity
def search(Head, val):
    curr=Head
    while curr:
        if val==curr.val:
            return True
        curr=curr.next
    return False

print(search(Head, 5))