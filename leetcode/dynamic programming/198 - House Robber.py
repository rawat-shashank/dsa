# Medium - 198 - House Robber

import unittest

class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1: return nums[0]
        dp = [*nums]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]

    def rob2(self, nums) -> int:
        if len(nums) == 1: return nums[0]
        n, m = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            m, n = max(m, nums[i] + n), m
        return m
            

def caller(nums):
    sl = Solution()
    return sl.rob2(nums)

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, caller(
            nums = [1,2,3,1]
        ))
        self.assertEqual(12, caller(
            nums = [2,7,9,3,1]
        ))

if __name__ == '__main__':
    unittest.main()