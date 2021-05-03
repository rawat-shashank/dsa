# Easy 237 - Delete Node in a Linked List - Success

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.val)
            printval = printval.next

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

        self.listprint()


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


# healper code
list = LinkedList()
list.head = ListNode(4)

e2 = ListNode(5)
e3 = ListNode(1)
e4 = ListNode(9)

list.head.next = e2
e2.next = e3
e3.next = e4

# list.listprint()

list.deleteNode(e3)
