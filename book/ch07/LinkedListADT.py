
class Node:
    
    __slots__ = '_node', '_next'

    def __init__(self, element=None, next=None):
        self._node = element
        self._next = next

class SinglyLinkedList:
    """
    Instance Variables :
       
    ADT :
        - prepend(value)    ->  Add a node in the beginning
        - append(value)     ->  Add a node in the end
        - pop()             ->  Remove a node from the end
        - popFirst()        ->  Remove a node from the beginning
    Other convenient methods:
        - head()        ->  Return the first node
        - tail()        ->  Return the last node
        - remove(Node)  ->  Remove Node from the list
        - traversal()
    """

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def head(self):
        if self._head == None:
            raise Empty("List is empty")
        return self._head._node
    
    def tail(self):
        if self._tail == None:
            raise Empty("List is empty")
        return self._tail._node

    def prepend(self, node):
        el = Node(el, self._head)
        if self.is_empty():
            self._tail = el
        self._head = el
        self._size += 1
    
    def append(self, node):
        el = Node(el, None)
        if self.is_empty():
            self._head = el
        self._tail._next = el 
        self._tail = el
        self._size += 1
    
    def pop_first(self):
        if self._head == None:
            raise Empty("List is empty")
        self._head = self._head._next
        self._size -= 1

    def pop(self):
        # not a good implementaion for complexity
