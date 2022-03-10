# Easy - 1941 - Check if All Characters Have Equal Number of Occurrences

import unittest

def firstTry(s):
    """
    accepted
    57 ms | 13.9 MB
    """
    dp = {}
    for x in s:
        dp[x] = dp.get(x, 0) + 1
    res = []
    for v in dp.values():
        if v not in res:
            res.append(v)
    return len(res) == 1


def caller(s):
    return firstTry(s)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(True, caller(
            s = "abacbc"
        ))
        self.assertEqual(False, caller(
            s = "aaabb"
        ))

if __name__ == '__main__':
    unittest.main()