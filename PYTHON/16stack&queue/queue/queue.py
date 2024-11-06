from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError("Dqueue from an empty queue")
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError('Peek from an empty queue')
        
    def print_queue(self):
        print("queue: ",list(self.queue))
if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.print_queue()
    print(q.size()) #4
    print(q.peek()) #Front of the queue: 1
    print(q.dequeue()) #1
    print(q.dequeue()) #2
    print(q.dequeue()) #3
    print(q.dequeue()) #4
    print(q.is_empty()) #True
        