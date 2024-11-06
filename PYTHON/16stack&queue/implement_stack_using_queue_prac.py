from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self,x:int)->None:
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.popleft())
    
    def pop(self)->int:
        if not self.empty():
            return self.q1.popleft()
        else:
            return -1
        
    def top(self)->int:
        if not self.empty():
            return self.q1[0]
        else:
            return -1
    def empty(self)->bool:
        return len(self.q1) == 0
    
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())
