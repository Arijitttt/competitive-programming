from collections import deque
class Stack(object):
    def __init__(self):
        self.arr = []
    def push(self,item):
        self.arr.append(item)
    def pop(self):
        if not self.is_empty():
            return self.arr.pop()
    def is_empty(self):
        return len(self.arr) == 0
    def peek(self):
        if not self.is_empty():
            return self.arr[-1]
    def size(self):
        return len(self.arr)
    
class Queue(object):
    def __init__(self):
        self.arr = deque()
    def enqueue(self,item):
        self.arr.append(item) 
    def deque(self):
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
        self.left = None
        self.right = None
class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)
    
    def print_tree(self,traversal_type):
        if traversal_type == 'preorder':
            return self.preOrder(tree.root,'')
        elif traversal_type == 'inorder':
            return self.inOrder(tree.root,'')
        elif traversal_type == 'postorder':
            return self.postOtder(tree.root,'')
        elif traversal_type == 'levelorder':
            return self.levelOrder(tree.root)
        elif traversal_type == 'reverselevelorder':
            return self.reverse_levelOrder(tree.root)
    def preOrder(self,start,traversal):
        #root left right
        if start:
            traversal += (str(start.value)+'-') 
            traversal = self.preOrder(start.left,traversal)
            traversal = self.preOrder(start.right,traversal)
        return traversal
    
    def inOrder(self,start,traversal):
        '''left root right'''
        if start:
            traversal = self.inOrder(start.left,traversal)
            traversal += (str(start.value)+'-')
            traversal = self.inOrder(start.right,traversal)
        return traversal
    
    def postOtder(self,start,traversal):
        '''left right root'''
        if start:
            traversal = self.postOtder(start.left,traversal)
            traversal = self.postOtder(start.right,traversal)
            traversal += (str(start.value)+'-')
        return traversal
    
    def levelOrder(self,start):
        if start is None:
            return
        queue = Queue()
        traversal = ''
        queue.enqueue(start)
        while queue.length() > 0:
            traversal += str(queue.peek().value) + '-'
            node = queue.deque()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal
    
    def reverse_levelOrder(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ''  # Initialize an empty string here

        while queue.length() > 0:
            node = queue.deque()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while stack.size() > 0:
            node = stack.pop()
            traversal += str(node.value) + '-'

        return traversal
    def height(self,node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height,right_height)
    
    def size(self):
        if self.root is None:
            return 0
        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack.size() > 0:
            node  = stack.pop()
            if node.left:
                size+=1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size
    def _size(self,node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
        
print(tree.print_tree('preorder'))
print(tree.print_tree('inorder'))
print(tree.print_tree('postorder'))
print(tree.print_tree('levelorder'))
print(tree.print_tree('reverselevelorder'))

print(tree.height(tree.root))
print(tree.size())
print(tree._size(tree.root))