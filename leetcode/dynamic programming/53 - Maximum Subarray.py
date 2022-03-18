# Easy - 53 - Maximum Subarray

import unittest

class Solution:
    def maxSubArray(self, nums) -> int:
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)

def caller(nums):
    sl = Solution()
    return sl.maxSubArray(nums)

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(6, caller(nums = [-2,1,-3,4,-1,2,1,-5,4]))
        self.assertEqual(1, caller(nums = [1]))
        self.assertEqual(23, caller(nums = [5,4,-1,7,8]))

if __name__ == '__main__':
    unittest.main()