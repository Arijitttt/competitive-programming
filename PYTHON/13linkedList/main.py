class Node:
    def __init__(self,data:None,next:None):
        self.data = data
        self.next = next
class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        
        node = Node(data,self.head)
        self.head = node
    def display(self):
        if self.head is None:
            print("ll is empty")
            return
        llstr = ''
        itr  = self.head
        while itr:
            llstr += str(itr.data)+'-->'
            itr = itr.next
        print(llstr)
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr  = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    def remove_at(self,index):
        if index< 0 or index>= self.get_length():
            raise Exception("invalid index")
        if index == 0 :
            self.head = self.head.next
        itr  = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next
    def insert_at(self,index,data):
        
        if index<0 or index>self.get_length():
            raise Exception("invalid index")
        if index == 0 :
            self.insert_at_beginning(data)
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next
if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(30)
    ll.insert_at_end(30)
    ll.remove_at(2)
    print(ll.get_length())
    ll.display()