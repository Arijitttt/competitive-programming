class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def level_order_traversal(root):
    if root is None:
        return
    
    queue = [root] 
    
    while queue:
        current_node = queue.pop(0)  
        print(current_node.data, end=" ")  
        
        
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)






# Constructing the binary tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

# Performing level order traversal
print("Level order traversal of the binary tree:")
level_order_traversal(root)
