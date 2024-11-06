class MyStack:
    def __init__(self):
        self.arr = []

    def push(self,data):
        self.arr.append(data)
        
    def pop(self):
        if len(self.arr) == 0 :
            return -1
        return self.arr.pop()

def process_quaries(quaries):
    stack = MyStack()
    result = []

    for query in quaries:
        if query[0] == 1:
            stack.push(query[1])
        elif query[0] == 2:
            result.append(stack.pop())
    return result

quaries = [(1, 2), (1, 3), (2,), (1, 4), (2,)]
output = process_quaries(quaries)
print(','.join(map(str, output)))