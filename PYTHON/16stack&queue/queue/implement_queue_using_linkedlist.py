class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.front is None
    def enqueue(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            print(f'enqueued {data} to queue')
        else:
            self.rear.next = new_node
            self.rear = new_node
            print(f'enqueued {data} to queue')
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            temp = self.front.value
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return temp
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            return self.front.value
    def get_queue(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.value)
            current = current.next
        return elements

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print('Front element is:', queue.peek())
queue.dequeue()
print('Queue:', queue.get_queue())
print('Front element after dequeue:', queue.peek())
print('Is queue empty?', queue.is_empty())