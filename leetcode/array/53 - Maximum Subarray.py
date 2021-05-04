# Easy - 53 - Maximum Subarray - Success
# Hint - kadane's algorithm


class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        currMax = outMax = nums[0]
        n = len(nums)
        for i in range(1, n):
            currMax = max(nums[i], currMax + nums[i])
            outMax = max(outMax, currMax)
            print(nums[i], currMax, outMax)
        return outMax


sol = Solution()
print(
    # sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    # sol.maxSubArray([5, 4, -1, 7, 8])
    sol.maxSubArray([1])
)
