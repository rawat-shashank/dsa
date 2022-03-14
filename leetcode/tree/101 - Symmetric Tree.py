# Easy - 101 - Symmetric Tree

import unittest
from listToBinaryTree import listToBinaryTree

class Solution:
    def isMirror(self, left, right):
        if left is None and right is None: return True
        if left is None or right is None: return False
        if left.val != right.val: return False

        outPair = self.isMirror(left.left, right.right)
        inPair = self.isMirror(left.right, right.left)
        return outPair and inPair

    def isSymmetric(self, root) -> bool:
        """
        50 ms | 14.1 MB
        """
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    
def caller(root):
    root = listToBinaryTree(root)
    sl = Solution()
    return sl.isSymmetric(root)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(True, caller(
            root = [1,2,2,3,4,4,3]
        ))
        self.assertEqual(False, caller(
            root = [1,2,2,None,3,None,3]
        ))
        self.assertEqual(False, caller(
            [1,2,3]
        ))

if __name__ == '__main__':
    unittest.main()