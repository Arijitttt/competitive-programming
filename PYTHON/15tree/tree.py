
class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def createNode(self,data):
        return Node(data)
    
    def insert(self,node,data):
        if node is None: 
            return self.createNode(data)
        if data<node.data:
            node.left=self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node

#driver code
# create a tree object
tree = Tree()
# create a root node with value 5
root  = tree.createNode(5)
# print the value of the root node
print(root.data) # output: 5


tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,7)
tree.insert(root,1)
tree.insert(root,15)
tree.insert(root,12)
tree.insert(root,20)
tree.insert(root,30)
tree.insert(root,6)
tree.insert(root,8)