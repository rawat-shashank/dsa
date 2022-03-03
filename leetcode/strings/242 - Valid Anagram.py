# Easy - 242 - Valid Anagram

import unittest

def firstTry(s, t):
    """
    Accpeted
    65 ms, faster than 59.18% of Python3 submissions
    14.5 MB, less than 45.98% of Python3 submissions
    """
    if len(s) != len(t):
        return False
    dp1, dp2 = {}, {}
    for x in s:
        dp1[x] = dp1.get(x, 0) + 1
    for x in t:
        dp2[x] = dp2.get(x, 0) + 1
    return dp1 == dp2

def secondTry(s, t):
    """
    Accpeted
    56 ms, faster than 74.23% of Python3 submissions
    14.5 MB, less than 75.15% of Python3 submissions
    """
    if len(s) != len(t):
        return False
    dp= {}
    for i in range(len(s)):
        dp[s[i]] = dp.get(s[i], 0) + 1
        dp[t[i]] = dp.get(t[i], 0) - 1
    
    for i in dp.values():
        if i != 0: return False
    return True
    
def caller(s, t):
    return secondTry(s, t)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(True, caller(
            s = "anagram",
            t = "nagaram"
        ))
        self.assertEqual(False, caller(
            s = "rat",
            t = "car"
        ))
        self.assertEqual(False, caller(
            s = "aacc",
            t = "ccac"
        ))

if __name__ == '__main__':
    unittest.main()