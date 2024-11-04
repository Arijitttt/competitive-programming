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