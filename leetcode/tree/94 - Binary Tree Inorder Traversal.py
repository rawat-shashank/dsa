import unittest
from listToBinaryTree import TreeNode
from typing import Optional, List

class Solution:
    def dfs(self, root, res):
        if root:
            self.dfs(root.left, res)
            self.dfs(root.right, res)
            res.append(root.val)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, res)
        return res


def caller(root):
    sl = Solution()
    return sl.inorderTraversal(root)

class Tests(unittest.TestCase):
    def test1(self):
        root = TreeNode(1)
        right = TreeNode(2)
        root.right = right
        right.left = TreeNode(3)
        self.assertEqual([1, 3, 2], caller(
            root
        ))
    def test2(self):
        root = TreeNode(1)
        self.assertEqual([1], caller(
            root
        ))

if __name__ == '__main__':
    unittest.main()