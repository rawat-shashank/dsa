import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dp, left, ans = {}, 0, 0
        for i, x in enumerate(s):
            if x in dp and left <= dp[x]:
                left = dp[x] + 1
            else:
                ans = max(ans, i-left+1)
            dp[x] = i
        return ans

def caller(s):
    sl = Solution()
    return sl.lengthOfLongestSubstring(s)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(3, caller(
            s = "abcabcbb"
        ))
        self.assertEqual(1, caller(
            s = "bbbbb"
        ))
        self.assertEqual(3, caller(
            s = "pwwkew"
        ))

if __name__ == '__main__':
    unittest.main()