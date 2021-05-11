# Easy - 141 - Linked List Cycle - Success

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def listprint(self, head):
        printval = head
        while printval is not None:
            print(printval.val)
            printval = printval.next

    def hasCycle(self, head: ListNode) -> bool:
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False


# healper code
list = Solution()
e1 = ListNode(1)

e2 = ListNode(2)
e1.next = e2

# e3 = ListNode(0)
# e2.next = e3

# e4 = ListNode(-4)
# e3.next = e4

# e5 = ListNode(5)
# e4.next = e2

# list.listprint(e1)
print("true" if list.hasCycle(e1) else "false")
