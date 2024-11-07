class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class MyStack:
    def __init__(self):
        self.head = None

    def push(self,data:int)->None:
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def pop(self)->int:
        if self.is_empty():
            return -1
        popped_item = self.head.value
        self.head = self.head.next
        return popped_item
    
    def top(self)->int:
        if self.is_empty():
            return -1
        return self.head.value
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