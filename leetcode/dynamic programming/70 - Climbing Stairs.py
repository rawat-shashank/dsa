# Easy - 70 - Climbing Stairs - success
# Hint use fibo with dp

class Solution:
    def __init__(self):
        self.dp = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        while n > 0:
            self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.dp[n]

        return self.dp[n]


sol = Solution()
climbStairs = sol.climbStairs(n=8)
print(climbStairs)
