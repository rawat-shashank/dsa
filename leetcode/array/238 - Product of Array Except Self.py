# Easy - 238 - Product of Array Except Self. - Success

class Solution:
    # brute force not accepted
    # def productExceptSelf(self, nums):
    #     out = []
    #     for i in range(len(nums)):
    #         val = 1
    #         for j in range(len(nums)):
    #             if val and i != j:
    #                 val = val * nums[j]
    #         out.append(val)
    #     return out

    def productExceptSelf(self, nums):
        out = []
        p = 1
        n = len(nums)
        for i in range(n):
            out.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1, -1, -1):
            print(i)
            out[i] = out[i] * p
            p = p * nums[i]

        return out


sol = Solution()
print(
    sol.productExceptSelf([1, 2, 3, 4])
    # sol.productExceptSelf([0, 0])
)


# 1 2 3 4
# 1 1 2 6

# solution explanation
# out 1 1 2 6(1 * 6) => p = 1 * 4
# out 1 1 8(4 * 2) 6 => p = 4 * 3
# out 1 12(12 * 1) 8 6 => p = 12 * 2
# out 24(24 *1) 12 8 6 => p = 24 * 1
