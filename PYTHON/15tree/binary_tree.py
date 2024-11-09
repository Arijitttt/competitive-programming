class Stack(object):
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def size(self):
        return len(self.items)
    def __len__(self):
        return self.size()


class Queue(object):
    def __init__(self):
        self.items = []
    
    def enqueue(self,item):
        self.items.insert(0,item)
    def deque(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)

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
            return self.preOrder_print(tree.root,'')
        elif traversal_type == 'inorder':
            return self.inOrder_print(tree.root,'')
        elif traversal_type == 'postorder':
            return self.postOrder_print(tree.root,'')
        elif traversal_type == 'levelorder':
            return self.levelOrder_print(tree.root)
        elif traversal_type == 'reverselevelorder':
            return self.reverse_levelOder_print(tree.root)
        else:
            print( 'Traversal type ' + traversal_type + ' is not supported')
            return False

    
    def preOrder_print(self,start,traversal):
        """ 
        ROOT -> LEFT -> RIGHT
        """
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preOrder_print(start.left,traversal)
            traversal = self.preOrder_print(start.right,traversal)
        return traversal
    
    def inOrder_print(self,start,traversal):
        """
        LEFT -> ROOT -> RIGHT
        """
        if start:
            traversal = self.inOrder_print(start.left,traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inOrder_print(start.right,traversal) 
        return traversal
    
    def postOrder_print(self,start,traversal):
        """
        LEFT -> RIGHT -> ROOT
        """
        if start:
            traversal = self.postOrder_print(start.left,traversal)
            traversal = self.postOrder_print(start.right,traversal)
            traversal += (str(start.value) + '-')
        return traversal
    

    # Level order Traversal
    def levelOrder_print(self,start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        
        traversal = ''

        while len(queue) > 0:
            traversal += str(queue.peek()) + '-'
            node  = queue.deque()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            
            
            
        return traversal
    
    def reverse_levelOder_print(self,start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ''
        while queue.size() > 0:
            node  = queue.deque()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        while stack.size() > 0:
            node = stack.pop()
            traversal += str(node.value) + '-'

        return traversal

#      1
#     /\
#    2  3
#   /\  /\
#  4 5 6  7
#         \
#          8

#1-2-4-5-3-6-7-8- (preorder traversal)
#4-2-5-1-6-3-7-8- (inorder traversal)
#4-5-2-6-8-7-3-1- (postorder traversal)
#1-2-3-4-5-6-7-8- (levelorder traversal)
#8-7-6-3-2-5-4-1- (reverse levelorder traversal)

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree.root.right.right.right = Node(8)



print(tree.print_tree('preorder') )
print(tree.print_tree('inorder') )
print(tree.print_tree('postorder') )

print(tree.print_tree('levelorder') )
print(tree.print_tree('reverselevelorder') )