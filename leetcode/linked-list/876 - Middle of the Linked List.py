# Easy - 876 - Middle of the Linked List - Success


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         arr = [head]
#         while arr[-1].next:
#             arr.append(arr[-1].next)
#         return arr[len(arr) // 2]

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
    
    def linkedListToList(self, head):
        ans = []
        printval = head
        while printval is not None:
            ans.append(printval.val)
            printval = printval.next
        return ans
    
    def middleNode(self, head: ListNode) -> ListNode:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]

    def middleNode2(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# healper code
def caller(head):
    ll = Solution()
    cur = dummy = ListNode(0)
    for x in head:
        cur.next = ListNode(x)
        cur = cur.next
    a = ll.middleNode2(dummy.next)
    return ll.linkedListToList(a)
    
    


class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual([3,4,5], caller(
            head = [1,2,3,4,5]
        ))
        self.assertEqual([4,5,6], caller(
            head = [1,2,3,4,5,6]
        ))

if __name__ == '__main__':
    unittest.main()