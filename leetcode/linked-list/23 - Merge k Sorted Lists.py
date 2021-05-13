# Hard - 23 - Merge k Sorted Lists - success
# use divide and conquer with merge two list.

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

    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
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

    def mergeKLists(self, lists):
        if not list or not len(lists):
            return None

        while len(lists) > 1:
            ul = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i+1 < len(lists) else None
                ul.append(self.merge_two_lists(l1, l2))
            lists = ul
        return lists[0]


# healper code
a1 = ListNode(1)
b1 = ListNode(1)
c1 = ListNode(2)

a2 = ListNode(4)
b2 = ListNode(3)
c2 = ListNode(6)

a1.next = a2
b1.next = b2
c1.next = c2

a3 = ListNode(5)
b3 = ListNode(4)
a2.next = a3
b2.next = b3

list = Solution()
h = list.mergeKLists(lists=[a1, b1, c1])
list.listprint(h)
# print("===")
# print("===")
# list.listprint(c1)
