class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data
    def setNext(self, nextnode):
        self.next = nextnode
    def getNext(self):
        return self.next
class LinkedList():
    def __init__(self):
        self.head = None
    def addNode(self, data):
        node = Node(data)
        node.setNext(self.head)
        self.head = node
    def printList(self):
        curr = self.head
        while curr is not None:
            print(curr.getData())
            curr = curr.getNext()
    def reverseList(self, curr, prev):
        
        if curr.getNext() is None:
            self.head = curr
            curr.setNext(prev)
            return
        next_value = curr.getNext()
 
        # And update next
        curr.setNext(prev)
 
        self.reverseList(next_value, curr)
            
    def reverse(self):
        curr = self.head
        if curr is None:
            return
        self.reverseList(curr,None)
        
        
llist = LinkedList()
llist.addNode(1)
llist.addNode(2)
llist.addNode(3)
llist.printList()
llist.reverse()
llist.printList()

    
