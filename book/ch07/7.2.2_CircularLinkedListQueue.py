class Node:
    __slots__ = '_node', '_next'

    def __init__(self, node=None, next=None):
        self._node = node
        self._next = next

class CircularQueue:
    """A class to represent a Stack using linked list.
    ...

    Attributes
    ----------
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
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if is_empty():
            raise ("Queue is Empty")
        head = self._tail._next
        retun head._node
    
    def dequeue(self):
        if is_empty():
            raise ("Queue is Empty")
        oldHead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldHead._next
        self._size -= 1
        return oldHead._node
    
    def enqueue(self, el):
        el = Node(el)
        if self.is_empty():
            el._next = el  # to make it circular, next pointing to itself if empty
        else:
            el._next = self._tail._next #new el next points to head
            self._tail._next = el   #old tail next point to new el
        self._tail = el  # new el is new tail
        self._size += 1
            
    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next
