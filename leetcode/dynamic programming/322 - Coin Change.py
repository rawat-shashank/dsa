# Medium - 322 - Coin Change - success

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return -1 if dp[amount] == amount+1 else dp[amount]


sol = Solution()
print(
    sol.coinChange(coins=[2], amount=1)
)
