# Meidum 641 design-circular-deque - Success

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = k
        self.data = [None] * self.size
        self.front = -1
        self.rear = -1

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.data[self.front] = value
        else:
            self.front = (self.front - 1) % self.size
            self.data[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.data[self.front] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.data[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        elif self.front == self.rear:
            self.data[self.front] = None
            self.front = -1
            self.rear = -1
        else:
            self.data[self.front] = None
            self.front = (self.front + 1) % self.size
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        elif self.front == self.rear:
            self.data[self.front] = None
            self.front = -1
            self.rear = -1
        else:
            self.data[self.rear] = None
            self.rear = (self.rear - 1) % self.size
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return -1 if self.isEmpty() else self.data[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return -1 if self.isEmpty() else self.data[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.rear + 1) % self.size == self.front


circularDeque = MyCircularDeque(3)
print(circularDeque.insertLast(1))
print(circularDeque.insertLast(2))
print(circularDeque.insertFront(3))
print(circularDeque.insertFront(4))
print(circularDeque.getRear())
print(circularDeque.isFull())
print(circularDeque.deleteLast())
print(circularDeque.insertFront(4))
print(circularDeque.getFront())
