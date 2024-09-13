class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class Linkedlist:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None) 
    

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def display(self):
        if self.head is None:
            print('linkedlist is empty')
            return
        llstr =''
        itr = self.head
        while itr:
            llstr += str(itr.data)+'-->'
            itr = itr.next
        print(llstr)

    def insert_after_values(self,data_after,data_to_insert):
        if self.head is None:
            self.head = Node(data_to_insert,None)
            return
        if self.head == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break
            itr = itr.next

    def remove_by_value(self,remove_data):
        if self.head is None:
            return
        if self.head.data == remove_data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == remove_data:
                itr.next = itr.next.next
                break
            itr = itr.next
if __name__=='__main__':
    ll = Linkedlist()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.display()
    ll.insert_after_values('mango','apple')
    ll.display()
    ll.remove_by_value('orange')
    ll.display()
