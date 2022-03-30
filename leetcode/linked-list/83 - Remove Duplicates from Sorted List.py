from multiprocessing import dummy
import unittest
from typing import Optional

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
    
    def linkedListToList(self, head):
        ans = []
        printval = head
        while printval is not None:
            ans.append(printval.val)
            printval = printval.next
        return ans
    
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1, head)
        while head and head.next is not None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return ans.next

# healper code
def caller(head):
    ll = Solution()
    cur = dummy = ListNode(0)
    for x in head:
        cur.next = ListNode(x)
        cur = cur.next
    
    a = ll.deleteDuplicates(dummy.next)
    return ll.linkedListToList(a)
    

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual([1,2], caller(
            head = [1,1,2]
        ))
        self.assertEqual([1, 2, 3], caller(
            head=[1,1,2,3,3]
        ))
        self.assertEqual([0], caller(
            head=[0,0,0,0,0]
        ))
        self.assertEqual([-1,0,3], caller(
            head=[-1,0,0,0,0,3,3]
        ))
        self.assertEqual([], caller(
            head=[]
        ))

if __name__ == '__main__':
    unittest.main()