# Easy - 566 - Reshape the Matrix

import unittest
from math import sqrt

class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        if len(mat) * len(mat[0]) != r * c: return mat
        ans = [[]]
        for row in mat:
            for item in row:
                if len(ans[-1]) >= c:
                    ans.append([])
                ans[-1].append(item)
        return ans
        
    
def caller(mat, r, c):
    sl = Solution()
    return sl.matrixReshape(mat, r, c)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual([[1,2,3,4]], caller(
            mat = [[1,2],[3,4]], r = 1, c = 4
        ))
        self.assertEqual([[1,2],[3,4]], caller(
            mat = [[1,2],[3,4]], r = 2, c = 4
        ))

if __name__ == '__main__':
    unittest.main()