# Hard 895 - maximum-frequency-stack - Success

class FreqStack:

    def __init__(self):
        self.list_stack = []
        self.el_freq = {}

    def push(self, val: int) -> None:
        temp = self.el_freq.get(val)
        if temp:
            self.el_freq[val] += 1
        else:
            self.el_freq[val] = 1

        try:
            temp = self.list_stack[self.el_freq[val] - 1]
            temp.append(val)
            self.list_stack[self.el_freq[val] - 1] = temp
        except IndexError:
            self.list_stack.insert((self.el_freq[val] - 1), [val])

        return None

    def pop(self) -> int:
        if len(self.list_stack[-1]) > 1:
            temp = self.list_stack[-1].pop()
        else:
            temp = self.list_stack.pop().pop()
        self.el_freq[temp] -= 1
        return temp


# Your FreqStack object will be instantiated and called as such:
freqStack = FreqStack()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)
freqStack.pop()
freqStack.pop()
freqStack.pop()
freqStack.pop()
