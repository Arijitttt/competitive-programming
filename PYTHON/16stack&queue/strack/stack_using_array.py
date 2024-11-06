class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
        print(f'pushed {item} to stack')
    
    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f'Popped {item} from stack')
            return item
        else:
            raise IndexError('pop from empty stack')
        
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError('Peek from an empty stack')
    def get_stack(self):
        return list(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print('Top element is: ',stack.peek())
print('stack size: ',stack.size())
stack.pop()
print('stack: ',stack.get_stack())
print('Top element after pop: ',stack.peek())
print('is stack empty? ',stack.is_empty())