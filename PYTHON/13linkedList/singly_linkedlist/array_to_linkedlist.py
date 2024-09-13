class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def array_to_linkedlist(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for i in range(1,len(arr)):
        current.next = Node(arr[i])
        current = current.next
    return head
def print_linkedlist(head):
    current  = head
    while current:
        print(current.data,end='->' if current.next else "")
        current = current.next
    print()

arr = [1,2,3,4,5]
head = array_to_linkedlist(arr)
print_linkedlist(head)