# Medium - 1721 - Swapping Nodes in a Linked List -

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.val)
            printval = printval.next

    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        outlist = []
        listnode = head
        while listnode:
            outlist.append(listnode)
            listnode = listnode.next
        el1 = outlist[k-1]
        el2 = outlist[-k]
        temp = el1.val
        el1.val = el2.val
        el2.val = temp

        return head

    # better solution using two pointer
    # def swapNodes(self, head: ListNode, k: int) -> ListNode:
    #     n1, n2, p = None, None, head
    #     while p is not None:
    #         k -= 1
    #         n2 = None if n2 == None else n2.next
    #         print(n2.val if n2 else None)
    #         if k == 0:
    #             n1 = p
    #             n2 = head
    #         p = p.next
    #     n1.val, n2.val = n2.val, n1.val
    #     return head


list = Solution()
list.head = ListNode(1)
e2 = ListNode(2)
e3 = ListNode(3)
e4 = ListNode(4)
e5 = ListNode(5)

list.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5

# list.listprint()
list.swapNodes(list.head, 2)
