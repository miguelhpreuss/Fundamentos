class Node:
    """Class Node"""
    def __init__(self, v):
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

    def __repr__(self):
        return str(self)
        
    def __str__(self):
        s = '['
        iter = self.head
        while iter != None:
            s = s + str(iter.v) + ', '
            iter = iter.next
        s = s.strip(', ') + ']'
        return s

    def __getitem__(self, index):
        if index >= self.length:
            raise IndexError('queue index out of range')
        iter = self.head
        for _ in range(index):
            iter = iter.next
        return iter.v

    def __setitem__(self, index, value):
        if index >= self.length:
            raise IndexError('queue index out of range')
        iter = self.head
        for _ in range(index):
            iter = iter.next
        iter.v = value   
    
    def enqueue(self, v):
        mynode = Node(v)
        if self.head == None:
            self.head = mynode
        else:
            self.tail.next = mynode
        self.tail = mynode
        self.length = self.length + 1

    def dequeue(self):
        if self.head == None:
            raise IndexError('dequeue from empty stack')
        v = self.head.v
        self.head = self.head.next
        self.length = self.length - 1
        return v

class Stack(Queue):
    """Classe Pilha"""
##    def enqueue(self, v):
##        mynode = Node(v)
##        if self.head == None:
##            self.tail = mynode
##        else:
##            mynode.next = self.head
##        self.head = mynode
##        self.length = self.length + 1
    def dequeue(self):
        if self.head == None:
            raise IndexError('dequeue from empty stack')
        v = self.tail.v
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            iter = self.head
            while iter.next != self.tail:
                iter = iter.next
            iter.next = None
            self.tail = iter
        return v    
    
fila = Queue()
fila.enqueue(5)
fila.enqueue(4)
fila.enqueue(3) 
print(len(fila))
print(fila)
##fila.dequeue()
##fila.dequeue()
##print(len(fila))
##fila.dequeue()
##
##try:
##    fila.dequeue()
##except:
##    print('Preste mais atenção, sua fila está vazia')
