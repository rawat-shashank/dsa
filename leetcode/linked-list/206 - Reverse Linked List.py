# Easy - 206 - Reverse Linked List - Success


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def __init__(self):
    #     self.head = None

    def listprint(self, head):
        printval = head
        while printval is not None:
            print(printval.val)
            printval = printval.next

    def reverseList(self, head: ListNode) -> ListNode:
        """Using iterative method, O(n)"""
        pn, cn = None, head
        while cn:
            nn = cn.next
            cn.next = pn
            pn = cn
            cn = nn
        return pn


# healper code
list = Solution()
e1 = ListNode(1)
e2 = ListNode(2)
e1.next = e2

e3 = ListNode(3)
e4 = ListNode(4)
e5 = ListNode(5)

e2.next = e3
e3.next = e4
e4.next = e5

# list.listprint(e1)
head = list.reverseList(e1)
list.listprint(head)
