from collections import deque
class Queue(object):
    def __init__(self):
        self.queue = deque()
    def enqueue(self,item):
        self.queue.append(item)
    def is_empty(self):
        return len(self.queue) == 0
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
    def size(self):
        return len(self.queue)
class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)
    def preOrder(self,start,traversal):
        # root left right
        if start: 
            traversal += (str(start.value)+ '-')
            traversal = self.preOrder(start.left,traversal)
            traversal = self.preOrder(start.right,traversal)
        return traversal
    def inOrder(self,start,traversal):
        if start:
            traversal = self.inOrder(start.left,traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inOrder(start.right,traversal)
        return traversal
    def postOrder(self,start,traversal):
        if start:
            traversal = self.postOrder(start.left,traversal)
            traversal = self.postOrder(start.right,traversal)
            traversal += (str(start.value) + '-')
        return traversal
    
    def levelOrder(self,start):
        if start is None:
            return
        queue = Queue()
        traversal = ''
        queue.enqueue(start)
        while queue.size() > 0:
            traversal += str(queue.peek().value) + '-'
            node  = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal
    
    def print_tree(self,traversalType):
        if traversalType == 'preorder':
            return self.preOrder(tree.root,'')
        elif traversalType == 'inorder':
            return self.inOrder(tree.root,'')
        elif traversalType == 'postorder':
            return self.postOrder(tree.root,'')
        elif traversalType == 'levelorder':
            return self.levelOrder(tree.root)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree('preorder'))
print(tree.print_tree('levelorder'))