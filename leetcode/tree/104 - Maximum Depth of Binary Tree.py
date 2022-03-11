# Easy - 104 - Maximum Depth of Binary Tree

import unittest
from listToBinaryTree import listToBinaryTree

class Solution:
    def maxDepth(self, root) -> int:
        """
        73 ms | 16.2 MB
        """
        d = 1
        if not root.left and not root.right:
            return 1
        l, r = 0, 0
        if root.left:
            l = self.maxDepth(root.left)
        if root.right:
            r = self.maxDepth(root.right)
        d += max(l, r)
        return d

    def secondTry(self, root) -> int:
        """
        36 ms | 16.2 MB
        """
        if not root: return 0
        return max(self.secondTry(root.left), self.secondTry(root.right)) + 1

    
def caller(root):
    root = listToBinaryTree(root)
    sl = Solution()
    return sl.secondTry(root)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(3, caller(
            root = [3,9,20,None, None,15,7]
        ))
        self.assertEqual(2, caller(
            root = [1,None,2]
        ))

if __name__ == '__main__':
    unittest.main()