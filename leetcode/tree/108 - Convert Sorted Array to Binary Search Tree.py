# Easy - 108 - Convert Sorted Array to Binary Search Tree

import unittest
from listToBinaryTree import TreeNode, isIdentical, listToBinaryTree

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        """
        129ms | 15.6 MB
        """
        def dfs(left, right):
            if left > right: return None
            mid = (left + right) // 2
            return TreeNode(
                nums[mid], dfs(left, mid - 1), dfs(mid+1, right)
            )
        return dfs(0, len(nums)- 1)

    
def caller(nums):
    sl = Solution()
    return sl.sortedArrayToBST(nums)

class Tests(unittest.TestCase):
    def test1(self):
        o1 = listToBinaryTree([0,-3,9,-10,None,5])
        o2 = listToBinaryTree([0,-10,5,None,-3,None,9])
        sol = caller([-10,-3,0,5,9])
        self.assertEqual(
            True, 
            (isIdentical(o1, sol) or isIdentical(o2, sol))
        )

    def test2(self):
        o1 = listToBinaryTree([1,None,3])
        o2 = listToBinaryTree([3,1])
        sol = caller([1, 3])
        self.assertEqual(
            True, 
            isIdentical(o1, sol) or isIdentical(o2, sol)
        )

if __name__ == '__main__':
    unittest.main()