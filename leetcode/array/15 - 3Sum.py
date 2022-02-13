# Medium 15 - 3 Sum - success

class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i, val in enumerate(nums):

            # check if prev element is same
            if i > 0 and val == nums[i-1]:
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                temp = nums[l] + val + nums[r]
                if temp < 0:
                    l += 1
                elif temp > 0:
                    r -= 1
                else:
                    res.append([nums[l], val, nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


sol = Solution()
threeSum = sol.threeSum([0, 0, 0, 0])
print(threeSum)
