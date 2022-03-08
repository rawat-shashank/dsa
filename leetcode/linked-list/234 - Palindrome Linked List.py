# Easy - 234 - Palindrome Linked List

import unittest

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

    def isPalindrome(self, head) -> bool:
        """
        Accepted
        1051 ms | 38.4 MB
        """
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            temp = slow.next
            slow.next, prev, slow = prev, slow, temp
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True


# healper code
def caller(head):
    ll = Solution()
    cur = dummy = ListNode(0)
    for x in head:
        cur.next = ListNode(x)
        cur = cur.next
    return ll.isPalindrome(dummy.next)
    


class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(True, caller(
            head = [1,2,2,1]
        ))
        self.assertEqual(False, caller(
            head = [1,2]
        ))

if __name__ == '__main__':
    unittest.main()