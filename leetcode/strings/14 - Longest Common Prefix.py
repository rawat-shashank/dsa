# Easy - 14 - Longest Common Prefix

import unittest

def firstTry(strs):
    """
    9:45
    9:49
    54ms | 14 MB
    """
    s1 = min(strs)
    s2 = max(strs)
    for i, ch in enumerate(s1):
        if ch != s2[i]: return s1[:i]
    return s1

def caller(strs):
    return firstTry(strs)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual('fl', caller(
            strs = ["flower","flow","flight"]
        ))
        self.assertEqual("", caller(
            strs = ["dog","racecar","car"]
        ))

if __name__ == '__main__':
    unittest.main()