# Easy - 326 - Power of Three

import unittest
from math import sqrt

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 3^19 =1162261467, 
	    # 3^20 is exceeding  Integer_Range So 3^19 is the highest power in Integer Range
        return n > 0 and 1162261467 % n == 0
    
def caller(n):
    sl = Solution()
    return sl.isPowerOfThree(n)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(True, caller(
            n = 27
        ))
        self.assertEqual(False, caller(
            n = 0
        ))
        self.assertEqual(True, caller(
            n=9
        ))

if __name__ == '__main__':
    unittest.main()