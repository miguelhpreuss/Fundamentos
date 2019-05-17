class Node:
    """Class Node"""
    def __init__(self,v):
        self.v = v
        self.next = None

class Queue:
    """Class Queue"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __len__(self):
        return self.length
    def __repr__ (self):
        return str(self)    
    def __str__(self):
        s = '['
        iter = self.head
        while iter != None:
            s=s+str(iter.v) + ','
            iter=iter.next
        s=s.strip(' , ')+']'
        return s

    def __getitem__(self, index):
        if index >= self.length:
            raise IndexError('queue index out of range')
        iter = self.head
        for _ in range(index):
            iter = iter.next
        return iter.value
    
    def __setitem__(self,index,value):
        if index >= self.length:
            raise IndexError('queue index out of range')
        iter = self.head
        for _ in range(index):
            iter = iter.next
        iter.v = value

    def enqueue(self,v):
        mynode = Node(v)
        if self.head == None:
            self.head = mynode
        else:
            self.tail.next = mynode
        self.tail = mynode
        self.length = self.length + 1

    def dequeue(self):
        if self.head == None:
            raise IndexError('deque from empty queue')
        v=self.head.v
        self.head = self.head.next
        self.length = self.length - 1
        return v
    
fila = Queue()
fila.enqueue(5)
fila.enqueue(4)
fila.enqueue(3)
print(fila)
print(len(fila))

try:
    fila.dequeue()
except:
    print('preste mais atencao sua fila esta vazia')
