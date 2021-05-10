# Medium - 33 - Search in Rotated Sorted Array - success

class Solution:
    def search(self, nums: [int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m
            else:
                if target < nums[m] or target > nums[r]:
                    r = m
                else:
                    l = m + 1
        return -1


sol = Solution()
print(
    sol.search([1], 1),
)
