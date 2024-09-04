class Node:
    def __init__(self,data=None,next =None):
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
            print('ll is empty')
            return
        llstr = ''
        itr = self.head
        while itr:
            llstr += str(itr.data)+'-->'
            itr = itr.next
        print(llstr)

if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_values([1,2,3,4])
    ll.display()