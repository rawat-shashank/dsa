
class Node:
    __slots__ = '_node', '_next'

    def __init__(self, node, next):
        self._node = node
        self._next = next

class LinkedStack:
    """A class to represent a Stack using linked list.
    ...

    Attributes
    ----------
    _head : Node
        first node to store the top or first node of linked list
    _size : Number
        storing the size of stack.

    Methods
    -------
    is_empty():
        check if the stack is empty
    push(el):
        push or add element 'el' at top of stack
    pop():
        gives the element by removing or poping top element from stack
    top():
        gives the element at top of stack without removing the element/
    """

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, el):
        self._head = Node(el, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise ("Stack empty")
        return self._head._node
    
    def pop(self):
        if self.is_empty():
            raise ("Stack empty")
        el = self._head._node
        self._head = self._head._next
        self._size -= 1
        return el
    

    