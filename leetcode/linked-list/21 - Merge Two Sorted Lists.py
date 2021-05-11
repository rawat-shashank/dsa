# Easy - 21 - Merge Two Sorted Lists - Success

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

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur = ListNode(None)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return head.next


# healper code
list = Solution()


e1 = ListNode(1)

e2 = ListNode(2)
e1.next = e2

e3 = ListNode(4)
e2.next = e3

l1 = ListNode(1)

l2 = ListNode(3)
l1.next = l2

l3 = ListNode(4)
l2.next = l3

# e4 = ListNode(-4)
# e3.next = e4

# e5 = ListNode(5)
# e4.next = e2

# list.listprint(e1)
# list.listprint(l1)

head = list.mergeTwoLists(e1, l1)
list.listprint(head)
