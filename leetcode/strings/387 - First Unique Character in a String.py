# Easy - 387 - First Unique Character in a String

import unittest

def firstTry(s):
    """
    Accpeted
    171 ms, faster than 45.38% of Python3 submissions.
    14 MB, less than 97.85% of Python3 submissions.
    """
    dp = {}
    for x in s:
        dp[x] = dp.get(x, 0) + 1
    
    res = -1
    print (dp)
    for i, v in dp.items():
        if v == 1:
            res = i
            break
    
    return res if res == -1 else s.index(res)
    
def caller(s):
    return firstTry(s)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(0, caller(
            s = "leetcode"
        ))
        self.assertEqual(2, caller(
            s = "loveleetcode"
        ))
        self.assertEqual(-1, caller(
            s = "aabb"
        ))

if __name__ == '__main__':
    unittest.main()