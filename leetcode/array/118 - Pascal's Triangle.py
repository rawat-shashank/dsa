# Easy - 118 - Pascal's Triangle

import unittest
from math import sqrt

class Solution:
    def generate(self, numRows: int):
        ans = [[1]*i for i in range(1, numRows+1)]
        for i in range(2, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1]
        return ans
        
    
def caller(numRows):
    sl = Solution()
    return sl.generate(numRows)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual([[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], caller(
            numRows = 5
        ))
        self.assertEqual([[1]], caller(
            numRows = 1
        ))

if __name__ == '__main__':
    unittest.main()