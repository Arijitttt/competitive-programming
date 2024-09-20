class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def prepend_node(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
    
    def append_node(self,data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node  = Node(data)
            cur = self.head
            while cur.next:
                cur  = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
    
    def add_after_node(self,key,data):
        cur  = self.head
        while cur:
            if cur.next is None and cur.data == key:
                new_node = Node(data)
                cur.next = new_node
                new_node.prev = cur
                new_node.next = None
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
            cur = cur.next
    def add_before_node(self,key,data):
        cur  = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                new_node = Node(data)
                new_node.prev = None
                new_node.next = cur
                cur.prev = new_node
                self.head = new_node
                return
            elif cur.data == key:
                new_node = Node(data)
                previous = cur.prev
                previous.next = new_node
                new_node.prev = previous
                new_node.next = cur
                cur.prev = new_node
            cur = cur.next
    
    def delete(self,key):
        cur  = self.head
        while cur:
            if cur.data == key and cur == self.head:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    nxt = cur.next
                    cur.next = None
                    cur = None
                    self.head = nxt
                    return
                
            elif cur.data == key:
                if cur.next:
                    nxt = cur.next
                    previous  = cur.prev
                    previous.next = nxt
                    nxt.prev = previous
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    previous = cur.prev
                    previous.next = None
                    cur.prev = None
                    cur = None
                    return

            cur  = cur.next
    
    def reverse(self):
        cur = self.head
        temp = None
        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
        if temp:
            self.head = temp.prev

    def print(self):
        cur = self.head
        while cur:
            print(cur.data, end='->' if cur.next else "")
            cur = cur.next

ddlst = DoublyLinkedList()
ddlst.prepend_node(1)
ddlst.prepend_node(2)
ddlst.prepend_node(3)
ddlst.append_node(4)
ddlst.append_node(5)
ddlst.add_after_node(2,6)
ddlst.add_before_node(3,7)
ddlst.delete(5)
ddlst.reverse()
ddlst.print()