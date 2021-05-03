# Easy 1 - Two Sum -

class Solution:
    def twoSum(self, nums, target: int):
        outDict = {}
        for idx, val in enumerate(nums):
            if val in outDict:
                return [outDict[val], idx]
            else:
                outDict[target - val] = idx
        return []


sol = Solution()
# twoSum = sol.twoSum(nums=[2, 7, 11, 15], target=9)
# twoSum = sol.twoSum(nums=[3, 2, 4], target=6)
twoSum = sol.twoSum(nums=[3, 3], target=6)
print(twoSum)
