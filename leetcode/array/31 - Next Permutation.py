import unittest
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                j = i
                while j < n and nums[j] > nums[i - 1]:
                    idx = j
                    j += 1
                nums[idx], nums[i - 1] = nums[i - 1], nums[idx]
                for k in range((n - i) // 2):
                    nums[i + k], nums[n - 1 - k] = nums[n - 1 - k], nums[i + k]
                break
        else:
            nums.reverse()
        return nums


def caller(nums):
    sl = Solution()
    return sl.nextPermutation(nums)


class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual([1, 3, 2], caller(nums=[1, 2, 3]))
        self.assertEqual([1, 2, 3], caller(nums=[3, 2, 1]))
        self.assertEqual([1, 5, 1], caller(nums=[1, 1, 5]))


if __name__ == "__main__":
    unittest.main()
