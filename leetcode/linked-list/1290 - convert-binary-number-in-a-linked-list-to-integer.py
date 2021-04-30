# Easy 1290 - convert-binary-number-in-a-linked-list-to-integer - Success

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def linkedListToString(self, head: ListNode) -> str:
        data = []
        while head.next:
            data.append(str(head.val))
            head = head.next
        data.append(str(head.val))
        return "".join(data)

    def getDecimalValue(self, head: ListNode) -> int:
        n = self.linkedListToString(head)

        return int(n, 2)

# better Solution

# num = head.val
#         while head.next:
#             num = num * 2 + head.next.val
#             head = head.next
