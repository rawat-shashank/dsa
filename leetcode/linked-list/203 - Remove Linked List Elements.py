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
    
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = dummy = ListNode(0, head)
        while dummy.next is not None:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        return ans.next

# healper code
def caller(head, val):
    ll = Solution()
    cur = dummy = ListNode(0)
    for x in head:
        cur.next = ListNode(x)
        cur = cur.next
    
    a = ll.removeElements(dummy.next, val)
    print("asdf ", ll.linkedListToList(a))
    return ll.linkedListToList(a)
    

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual([1,2,3,4,5], caller(
            head = [1,2,6,3,4,5,6], val = 6
        ))
        self.assertEqual([], caller(
            head = [], val = 1
        ))
        self.assertEqual([], caller(
            head = [7,7,7,7], val = 7
        ))
        self.assertEqual([2], caller(
            head=[1,2], val=1
        ))

if __name__ == '__main__':
    unittest.main()