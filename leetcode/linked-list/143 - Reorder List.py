# Medium - 143 - Reorder List - success

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

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head:
            return

        # find middle
        s = f = head
        while f and f.next and f.next.next:
            s = s.next
            f = f.next.next

        # reverse the remaining list
        pn, cn = None, s.next
        while cn:
            nn = cn.next
            cn.next = pn
            pn = cn
            cn = nn
        s.next = None

        # merge both
        h1, h2 = head, pn
        while h2:
            nn = h1.next
            h1.next = h2
            h1 = h2
            h2 = nn

        self.listprint(head)


# healper code
list = Solution()
e1 = ListNode(1)

e2 = ListNode(2)
e1.next = e2

e3 = ListNode(3)
e2.next = e3

e4 = ListNode(4)
e3.next = e4

e5 = ListNode(5)
e4.next = e5

e6 = ListNode(6)
e5.next = e6

# list.listprint(e1)
list.reorderList(head=e1)
