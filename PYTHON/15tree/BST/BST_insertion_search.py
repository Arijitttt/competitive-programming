class Node(object):
    def __init__(self, value= None):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None 

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else: 
            self._insert(data,self.root)
    
    def _insert(self,data,cur_node):
        if data < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data,cur_node.left)
        elif data > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data,cur_node.right)
        else:
            print("Data is already in the tree")
    

    def search(self,data):
        if self.root:
            is_found = self._search(data,self.root)
            if is_found:
                return True
            return False
        else:
            return None
    
    def _search(self,data,cur_node):
        if data > cur_node.value and cur_node.right: 
            return self._search(data,cur_node.right)
        elif data < cur_node.value and cur_node.left:
            return self._search(data,cur_node.left)
        if data == cur_node.value:
            return True

bst = BST()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)

print(bst.search(2))