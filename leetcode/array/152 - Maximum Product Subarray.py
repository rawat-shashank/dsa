# Medium - 152 - Maximum Product Subarray - Success

class Solution:
    # def maxProduct(self, nums: [int]) -> int:
    # prefix, suffix, max_so_far = 0, 0, float('-inf')
    # for i in range(len(nums)):
    #     prefix = (prefix or 1) * nums[i]
    #     suffix = (suffix or 1) * nums[~i]
    #     max_so_far = max(max_so_far, prefix, suffix)
    #     print(prefix, suffix, max_so_far)
    # return max_so_far

    #  Better solution
    def maxProduct(self, nums: [int]) -> int:
        curMax = curMin = prod = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                temp = curMax
                curMax = curMin
                curMin = temp
            curMax = max(nums[i], nums[i] * curMax)
            curMin = min(nums[i], nums[i] * curMin)
            prod = max(prod, curMax)
        return prod


sol = Solution()
print(
    # sol.maxProduct([2, 3, -2, 4])
    sol.maxProduct([-2, 0, -1])
)
