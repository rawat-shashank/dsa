# Medium - 98 - Validate Binary Search Tree

import unittest
from listToBinaryTree import listToBinaryTree

class Solution:
    def isValidBST(self, root, min=float('-inf'), max=float('inf')) -> bool:
        """
        64 ms | 16.6 MB
        """
        if not root: return True
        if min >= root.val or max <= root.val: return False
        return self.isValidBST(root.left, min, root.val) and self.isValidBST(root.right, root.val, max)

    
def caller(root):
    root = listToBinaryTree(root)
    sl = Solution()
    return sl.isValidBST(root)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(True, caller(
            root = [2,1,3]
        ))
        self.assertEqual(False, caller(
            root = [5,1,4,None,None,3,6]
        ))
        self.assertEqual(False, caller(
            root=[2,2,2]
        ))
        self.assertEqual(False, caller(
            root=[5,4,6,None,None,3,7]
        ))

if __name__ == '__main__':
    unittest.main()