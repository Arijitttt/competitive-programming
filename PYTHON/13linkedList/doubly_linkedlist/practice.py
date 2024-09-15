class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLInkedlist:
    def __init__(self):
        self.head  = None

    def append_node(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
    
    def prepend_node(self,data):
        if self.head is None:
            new_Node = Node(data)
            new_Node.prev = None
            self.head = new_Node
        else:
            newNode = Node(data)
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            newNode.prev = None
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data,end='->' if cur.next else '')
            cur = cur.next

ddlst = DoublyLInkedlist()
ddlst.append_node(1)
ddlst.prepend_node(2)
ddlst.append_node(4)
ddlst.append_node(5)
ddlst.print_list()