# Easy - 13 - Roman to Integer

import unittest
from math import sqrt

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res, prev = 0, 'I'
        for i in s[::-1]:
            res, prev = res - d[i] if d[i] < d[prev] else res + d[i], i
            print(res, prev)
        return res
    
def caller(s):
    sl = Solution()
    return sl.romanToInt(s)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(3, caller(
            s = "III"
        ))
        self.assertEqual(58, caller(
            s = "LVIII"
        ))
        self.assertEqual(1994, caller(
            s = "MCMXCIV"
        ))

if __name__ == '__main__':
    unittest.main()