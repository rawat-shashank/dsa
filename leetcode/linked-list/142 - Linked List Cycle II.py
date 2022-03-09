# Medium - 142 - Linked List Cycle II

import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head) -> bool:
        """
        Accepted
        84 ms | 17.4 MB
        """
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                break
        else:
            return None

        while head is not s:
            head = head.next
            s = s.next
        return head
    
# healper code
def caller(head, pos):
    ll = Solution()
    cur = dummy = temp = ListNode(0)
    for x in head:
        cur.next = ListNode(x)
        cur = cur.next
    if pos > -1:
        for _ in range(pos):
            temp = temp.next
        cur.next = temp.next
    temp = ll.detectCycle(dummy.next)
    return temp.val if temp else None
    


class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(2, caller(
            head = [3,2,0,-4], pos = 1
        ))
        self.assertEqual(1, caller(
            head = [1,2], pos = 0
        ))
        self.assertEqual(None, caller(
            head = [1], pos = -1
        ))

if __name__ == '__main__':
    unittest.main()