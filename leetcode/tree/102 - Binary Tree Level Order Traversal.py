# Medium - 102 - Binary Tree Level Order Traversal

import unittest
from listToBinaryTree import listToBinaryTree

class Solution:
    def levelOrder(self, root) -> bool:
        """
        45ms | 14.1 MB
        """
        if not root: return []
        queue, res = [root], []
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(level)
        return res

    
def caller(root):
    root = listToBinaryTree(root)
    sl = Solution()
    return sl.levelOrder(root)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual([[3],[9,20],[15,7]], caller(
            root = [3,9,20,None,None,15,7]
        ))
        self.assertEqual([[1]], caller(
            root = [1]
        ))
        self.assertEqual([], caller(
            []
        ))

if __name__ == '__main__':
    unittest.main()