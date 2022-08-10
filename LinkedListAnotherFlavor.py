class Node:
    
'''
create a class to hold data as well as a link to next element
params: data will be our input that needs to be in linked list
        next will hold reference to new input/data
'''
    def __init__(self,data, next):
        self.data = data
        self.next = next

class LinkedList:
    
'''
create a class where constructor will define a variable called 
head that holds Node instance.
after defining the Node class, we will assign that to head.
head will be acting as point of entry for all linked list
operations
'''
    def __init__(self, head=None):
        self.head = None
    
    # Node instance will be created for each input and gets assigned to head
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
    
    #to insert a list of inputs at a time
    def insert_list(self, list):
        self.head = None
        
        for item in list:
            self.insert_at_begin(item)
            
    #to get len of the linked list
    def get_len(self):
        
        if self.head is None:
            return 0
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    #to insert element at given index, not appending though
    def insert_at_index(self,index,data):
        
        itr = self.head
        count = 0
        while itr:
            
            if count == index-1:
                itr.next = Node(data,itr.next.next)
                break
            count+=1
            itr = itr.next
        
ll = LinkedList()

ll.insert_list([1,2,3,4])
ll.print()
ll.insert_at_index(2,5)

ll.print()
