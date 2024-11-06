class MyQueue:
    def __init__(self):
        self.stack_in = [] # stack used for pushing new elements
        self.stack_out = [] # stack used for popping elements in FIFO order
    
    def push(self,x:int)->None:
        self.stack_in.append(x)

    def pop(self)-> int:
        # if stack_out is empty, move all the elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if self.stack_out:
            return self.stack_out.pop()
        else:
            return -1
        
    def peek(self)->int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if self.stack_out:
            return self.stack_out[-1]
        else:
            return -1

    def empty(self)->bool:
        if not self.stack_in and not self.stack_out:
            return True
        else:
            return False
        
myQueue = MyQueue()
myQueue.push(1)      # Queue is: [1]
myQueue.push(2)      # Queue is: [1, 2] (front is 1, back is 2)
print(myQueue.peek()) # Output: 1
print(myQueue.pop())  # Output: 1
print(myQueue.empty())# Output: False