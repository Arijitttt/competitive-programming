class Node:
    def __init__(self,data:None,next:None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head = node
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr  = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    def get_lengh(self):
        count  = 0
        itr  = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    def remove_at(self,index):
        if index<0 or index>=self.get_lengh():
            raise Exception("invalid index")
        if index == 0 :
            self.head = self.head.next
        count = 0
        itr  = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            count += 1
    def insert_at(self,index,data):
        if index<0 or index>=self.get_lengh():
            raise Exception("invalid index")
        if index == 0 :
            self.insert_at_beginning(data)
        count  = 0
        itr  =  self.head
        while itr:
            if  count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            count += 1
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(21)
    ll.insert_at_beginning(22)
    ll.remove_at(1)
    ll.insert_at(1,23)
    ll.print()
