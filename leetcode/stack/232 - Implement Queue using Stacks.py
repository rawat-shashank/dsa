import unittest

from numpy import empty

class MyQueue:

    def __init__(self):
        self.input, self.output = [], []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if self.output == []:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []

class Tests(unittest.TestCase):
    def tests(self):
        s = MyQueue()
        s.push(1)
        s.push(2)
        self.assertEqual(s.peek(), 1)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.empty(), False)

if __name__ == '__main__':
    unittest.main()