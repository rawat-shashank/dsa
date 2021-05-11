# Medium - 19 - Remove Nth Node From End of List - Success

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def listprint(self, head):
        printval = head
        while printval is not None:
            print(printval.val)
            printval = printval.next

    def removeNthFromEnd(self, head: ListNode, n: int):
        d = ListNode(0, head)
        s, f = d, head
        while n > 0:
            f = f.next
            n -= 1

        while f:
            s = s.next
            f = f.next

        s.next = s.next.next

        return d.next


# healper code
list = Solution()
e1 = ListNode(1)

e2 = ListNode(2)
e1.next = e2

# e3 = ListNode(3)
# e2.next = e3

# e4 = ListNode(4)
# e3.next = e4

# e5 = ListNode(5)
# e4.next = e5

# list.listprint(e1)
head = list.removeNthFromEnd(head=e1, n=2)
list.listprint(head)
