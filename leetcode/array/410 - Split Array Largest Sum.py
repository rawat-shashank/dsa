import unittest
from typing import List

class Solution:
    def canSplit(self, nums: List[int], largest: int, m: int):
        subarray, curSum = 0, 0
        for n in nums:
            curSum += n
            if curSum > largest:
                subarray += 1
                curSum = n
        return subarray + 1 <= m

    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        res = right
        while left <= right:
            mid = (left + right) // 2
            if self.canSplit(nums, mid, m):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

        

def caller(nums, m):
    sl = Solution()
    return sl.splitArray(nums, m)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(18, caller(
            nums = [7,2,5,10,8], m = 2
        ))
        self.assertEqual(9, caller(
            nums = [1,2,3,4,5], m = 2
        ))
        self.assertEqual(4, caller(
            nums = [1,4,4], m = 3
        ))

if __name__ == '__main__':
    unittest.main()