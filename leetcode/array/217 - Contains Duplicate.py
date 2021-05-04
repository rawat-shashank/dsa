# Easy - 217 - Contains Duplicate - Success

class Solution:
    def containsDuplicate(self, nums) -> bool:
        data = {}
        for x in nums:
            if x in data:
                return True
            else:
                data[x] = x
        return False


sol = Solution()
print(
    sol.containsDuplicate([1, 2, 3])
)
