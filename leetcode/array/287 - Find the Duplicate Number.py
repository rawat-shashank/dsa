import unittest
from math import sqrt
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        0837
        0839
        """
        dp = {}
        for x in nums:
            if dp.get(x): return x
            dp[x] = 1
    
    def findDuplicate2(self, nums: List[int]) -> int:
        seen = 0
        for num in nums:
            if seen & (1 << num):
                return num
            seen |= 1 << num

    
def caller(nums):
    sl = Solution()
    return sl.findDuplicate2(nums)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(2, caller(
            nums = [1,3,4,2,2]
        ))
        self.assertEqual(3, caller(
            nums = [3,1,3,4,2]
        ))

if __name__ == '__main__':
    unittest.main()