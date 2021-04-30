
class ArrayQueue:
    """
    Instance Variables :
        - _data     =>  is a reference to a list instance with a fixed capacity.
        - _size     =>  is an integer representing the current number of elements stored
                        in the queue (as opposed to the length of the data list).
        - _front    =>  is an integer that represents the index within data of the first
                        element of the queue (assuming the queue is not empty).
    ADT :
        - enqueue()
        - dequeue()
    Other convenient methods:
        - __len__()
        - is_empty()
        - first()
    """

    _DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * ArrayQueue._DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        return self._data[self._front]
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        elem = self._data[self._front];
        self._data[self._front] = None;
        self._front = (self._front + 1) % len(self._data)
        self._size -=1
        return elem
    
    def _resize(self, new_cap):
        old = self._data
        self._data = [None] * new_cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size +=1
