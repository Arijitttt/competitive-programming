class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class MyStack:
    def __init__(self):
        self.head = None #Head of the linked list represents the top of the stack

    def push(self,x:int)->None:
        new_node = Node(x) #create a anew node with the given value
        new_node.next = self.head #make the new node point to the current head
        self.head = new_node # Update head to the new node, making it the top of the stack
    
    def pop(self)->int:
        if self.is_empty():
            return -1
        popped_value = self.head.value # Get the value from the top node
        self.head = self.head.next # Move the head to the next node, removing the top node
        return popped_value
    
    def top(self)->int:
        if not self.is_empty():
            return self.head.value
        else:
            return -1
        
    def is_empty(self)->bool:
        return self.head == None
    
stack = MyStack()
stack.push(10)
stack.push(20)
print(stack.top())
print(stack.pop())
print(stack.is_empty())
print(stack.pop())
print(stack.is_empty())