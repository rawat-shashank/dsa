class Node:
    __slots__ = '_node', '_next'

    def __init__(self, node=None, next=None):
        self._node = node
        self._next = next

class LinkedStack:
    """A class to represent a Stack using linked list.
    ...

    Attributes
    ----------
    _head : Node
        first node to store the top or first node of linked list
    _tail : Node
        last node to store the top or first node of linked list
    _size : Number
        storing the size of stack.

    Methods
    -------
    is_empty():
        check if the queue is empty
    enqueue(el):
        insert el at the last of queue
    dequeue():
        remove and return first in element in queue.
    first():
        gives the first in element in queue without removing the element
    """

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if is_empty():
            raise ("Queue is Empty")
        retun self._head._node
    
    def dequeue(self):
        if is_empty():
            raise ("Queue is Empty")
        el = self._head._node
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return el
    
    def enqueue(self, el):
        el = Node(el)
        if self.is_empty():
            self._head = el
        else:
            self.tail._next = el #update prev tail to save new ele ref
        self._tail = el  # update tail to new ele
        self._size += 1
            
