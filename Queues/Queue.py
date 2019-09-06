class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    
    def enqueue(self,val):
        newNode = Node(val)
        if (self.size == 0):
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        
        self.size += 1
        return self.size
    
    def dequeue(self):
        if (self.size == 0):
            return None
        temp = self.first
        if (self.first == self.last):
            self.last = None
        
        self.first = self.first.next
        
        self.size -= 1
        return temp.value


q = Queue()
q.enqueue(5)
q.enqueue(6)
print(q.enqueue(7))
print(q.enqueue(8))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q)

