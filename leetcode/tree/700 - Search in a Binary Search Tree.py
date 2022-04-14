
import unittest
from typing import Optional, List
from listToBinaryTree import listToBinaryTree, TreeNode


class Solution:
    def dfs(self, root, res):
        if root:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root
            root = root.right if val > root.val else root.left
        return None


def caller(root, val):
    root = listToBinaryTree(root)
    sl = Solution()
    ans = sl.searchBST(root, val)
    return sl.preorderTraversal(ans) if ans else []


class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual([2, 1, 3], caller(
            root=[4, 2, 7, 1, 3], val=2
        ))
        self.assertEqual([], caller(
            root = [4,2,7,1,3], val = 5
        ))


if __name__ == '__main__':
    unittest.main()
