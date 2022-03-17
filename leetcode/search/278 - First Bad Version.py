# Easy - 278 - First Bad Version

import unittest

class Solution:
    def __init__(self, bad) -> None:
        self.bad = bad

    def isBadVersion(self, version: int) -> bool:
        return self.bad == version

    def firstBadVersion(self, n) -> int:
        """
        55ms | 13.9 MB
        """
        i, j = 1, n
        while i < j:
            mid = (i + j) // 2
            if self.isBadVersion(mid): j = mid
            else: i = mid + 1
        return i

    
def caller(n, bad):
    sl = Solution(bad)
    return sl.firstBadVersion(n)

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, caller(n=5, bad=4))
        self.assertEqual(1, caller(n=1, bad=1))

if __name__ == '__main__':
    unittest.main()