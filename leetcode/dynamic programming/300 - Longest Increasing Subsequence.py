# Medium - 300 - Longest Increasing Subsequence - success

import unittest


class Solution:
    def lengthOfLIS(self, nums) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        print(LIS)
        return max(LIS)


class TestMissingNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_lengthOfLIS(self):
        print("test lengthOfLIS")
        self.assertEqual(4, self.sol.lengthOfLIS(
            nums=[10, 9, 2, 5, 3, 7, 101, 18]))
        self.assertEqual(4, self.sol.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))
        self.assertEqual(1, self.sol.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]))


if __name__ == '__main__':
    unittest.main()
