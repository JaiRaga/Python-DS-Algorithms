class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, val):
        newNode = Node(val)
        if (not self.first):
            self.first = newNode
            self.last = newNode
        else:
            temp = self.first
            self.first = newNode
            self.first.next = temp
        
        self.size += 1
        return self.size
    
    def pop(self):
        if (self.size == 0):
            return None
        
        temp = self.first
        if (self.first == self.last):
            self.last = None
        else:
            self.first = self.first.next
        
        self.size -= 1
        return temp.value
    
s = Stack()
s.push(5)
s.push(6)
print(s.push(7))
print(s.pop())
print(s.pop())
print(s.pop())
print(s.size)
