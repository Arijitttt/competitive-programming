"""
Stack Data Structure

A B C D
->
D
C
B
A

"""
class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

print(s.peek())
print(s.get_stack())
print(s.pop())
print(s.get_stack())
