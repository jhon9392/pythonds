class Node:
    
    #defining constructor
    def __init__(self,data, next):
        self.data = data
        self.next = next

class LinkedList:
    
    #defining constructor
    def __init__(self, head=None):
        self.head = None
    
    def insert_at_begin(self, data):
        n = Node(data,self.head)
        self.head = n
        
    def print(self):
        
        if self.head is None:
            return print('its empty')
        
        itr = self.head
        ll = ''
        while itr:
            ll += str(itr.data) + '-->'
            itr = itr.next
        return print(ll)
    
    def insert_list(self, list):
        self.head = None
        
        for item in list:
            self.insert_at_begin(item)
    def get_len(self):
        
        if self.head is None:
            return 0
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
        
ll = LinkedList()
print(ll.get_len())
ll.insert_at_begin(5)
print(ll.get_len())
ll.insert_at_begin(55)
print(ll.get_len())
ll.insert_list([1,2,3,4])

print(ll.get_len())
