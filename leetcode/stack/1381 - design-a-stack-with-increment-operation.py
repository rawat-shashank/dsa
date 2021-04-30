# Medium 1381 - design-a-stack-with-increment-operation - success

class CustomStack:

    class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.data = []

    def push(self, x: int) -> None:
        if len(self.data) < self.maxSize:
            self.data.append(x)

    def pop(self) -> int:
        return -1 if len(self.data) == 0 else self.data.pop()

    def increment(self, k: int, val: int) -> None:
        self.data = [x + val if idx < k else x for idx,
                     x in enumerate(self.data)]


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


# Input
# ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
# [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
# Output
# [null,null,null,2,null,null,null,null,null,103,202,201,-1]
# Explanation
# CustomStack customStack = new CustomStack(3); // Stack is Empty []
# customStack.push(1);                          // stack becomes [1]
# customStack.push(2);                          // stack becomes [1, 2]
# customStack.pop();                            // return 2 --> Return top of the stack 2, stack becomes [1]
# customStack.push(2);                          // stack becomes [1, 2]
# customStack.push(3);                          // stack becomes [1, 2, 3]
# customStack.push(4);                          // stack still [1, 2, 3], Don't add another elements as size is 4
# customStack.increment(5, 100);                // stack becomes [101, 102, 103]
# customStack.increment(2, 100);                // stack becomes [201, 202, 103]
# customStack.pop();                            // return 103 --> Return top of the stack 103, stack becomes [201, 202]
# customStack.pop();                            // return 202 --> Return top of the stack 102, stack becomes [201]
# customStack.pop();                            // return 201 --> Return top of the stack 101, stack becomes []
# customStack.pop();                            // return -1 --> Stack is empty return -1.
