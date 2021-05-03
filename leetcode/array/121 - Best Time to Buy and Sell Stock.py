# Easy - 121 - Best Time to Buy and Sell Stock - Success


class Solution:
    def maxProfit(self, prices) -> int:
        min_Val, profit = float('inf'), 0
        for x in prices:
            profit = max(profit, x - min_Val)
            min_Val = min(x, min_Val)
        return profit


sol = Solution()
print(
    sol.maxProfit([7, 1, 5, 3, 6, 4])
)

# print(
#     sol.maxProfit([2, 4, 1])
# )
