# Medium - 11 - Container With Most Water - success

class Solution:
    def maxArea(self, height: [int]) -> int:
        maxArea = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            maxArea = max(maxArea, area)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return maxArea


sol = Solution()
# maxArea = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
# maxArea = sol.maxArea([1, 1])
# maxArea = sol.maxArea([4, 3, 2, 1, 4])
# maxArea = sol.maxArea([1, 2, 1])
# maxArea = sol.maxArea([0, 2])
# maxArea = sol.maxArea([2, 3, 10, 5, 7, 8, 9])
print(maxArea)
