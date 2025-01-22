class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def print(self):
        current = self.head
        llstr = ''
        while current:
            llstr += str(current.data) + '-->'
            current = current.next
        print(llstr)
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
ll = Linkedlist()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

print("Original Linked List:")
ll.print()

ll.reverse()
print("Reversed Linked List:")
ll.print()