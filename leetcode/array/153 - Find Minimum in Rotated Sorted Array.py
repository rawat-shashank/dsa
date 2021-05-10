# Medium - 153 - Find Minimum in Rotated Sorted Array - Success
# Hint - use binary search tree


class Solution:
    def findMin(self, nums: [int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:

            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


sol = Solution()
print(
    sol.findMin([1, 2, 3, 4, 5]),
)
