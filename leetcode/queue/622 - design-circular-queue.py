# Meidum 622 - design-circular-queue - Success

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.data = [None] * self.size
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
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

    def deQueue(self) -> bool:
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

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.data[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front


# Your MyCircularQueue object will be instantiated and called as such:
myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(1))
print(myCircularQueue.enQueue(2))
print(myCircularQueue.enQueue(3))
print(myCircularQueue.deQueue())
print(myCircularQueue.deQueue())
print(myCircularQueue.enQueue(5))
print(myCircularQueue.enQueue(3))
print(myCircularQueue.deQueue())
print(myCircularQueue.deQueue())
print(myCircularQueue.deQueue())
print(myCircularQueue.deQueue())
