from collections import deque
class Queue(object):
    def __init__(self):
        self.arr = deque()
    def enqueue(self,item):
        self.arr.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.arr.popleft()
    def is_empty(self):
        return len(self.arr) == 0
    def peek(self):
        if not self.is_empty():
            return self.arr[0]
    def length(self):
        return len(self.arr)
class Node(object):
    def __init__(self,value):
        self.value = value
        self .left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def preOrder(self,start,traversal):
        '''root left right'''
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preOrder(start.left,traversal)
            traversal = self.preOrder(start.right,traversal)
        return traversal
    
    def inorder(self,start,traversal):
        # left root right
        if start:
            traversal = self.inorder(start.left,traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder(start.right,traversal)

        return traversal
    
    def postOrder(self,start,traversal):
        # left right root
        if start:
            traversal = self.postOrder(start.left,traversal)
            traversal = self.postOrder(start.right,traversal)
            traversal += (str(start.value) + '-')
        return traversal
    
    def levelorder(self,start):
        if start is None: 
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ''
        while queue.length() > 0:
            traversal += str(queue.peek().value) + '-'
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal
    
    def printTree(self,traversal_type):
        if traversal_type == 'preorder':
            return self.preOrder(tree.root,'')
        elif traversal_type == 'inorder':
            return self.inorder(tree.root,'')
        elif traversal_type == 'postorder':
            return self.postOrder(tree.root,'')
        elif traversal_type == 'levelorder':
            return self.levelorder(tree.root)
        else:
            print( 'Traversal type ' + traversal_type + ' is not supported')
            return False


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.printTree('preorder'))
print(tree.printTree('levelorder'))