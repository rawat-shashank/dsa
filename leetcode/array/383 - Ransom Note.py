import unittest
from math import sqrt
from typing import List

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote): return False
        dp = {}
        for x in ransomNote:
            dp[x] = dp.get(x, 0) + 1
        for x in magazine:
            dp[x] = dp.get(x, 0) - 1
        for x in dp.values():
            if x > 0: return False
        return True
    
def caller(ransomNote, magazine):
    sl = Solution()
    return sl.canConstruct(ransomNote, magazine)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(True, caller(
            ransomNote = "aa", magazine = "aab"
        ))
        self.assertEqual(False, caller(
            ransomNote = "aa", magazine = "ab"
        ))
        self.assertEqual(False, caller(
            ransomNote = "a", magazine = "b"
        ))
        self.assertEqual(True, caller(
            ransomNote = "bg", magazine="efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
        ))

if __name__ == '__main__':
    unittest.main()