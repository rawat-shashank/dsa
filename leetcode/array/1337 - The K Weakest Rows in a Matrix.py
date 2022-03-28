# Easy - 1337 - The K Weakest Rows in a Matrix

import unittest

class Solution:
    def kWeakestRows(self, mat, k: int):
        return sorted(range(len(mat)), key=lambda x: mat[x])[:k]

        
    
def caller(mat, k):
    sl = Solution()
    return sl.kWeakestRows(mat, k)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual([2,0,3], caller(
            mat = 
            [[1,1,0,0,0],
            [1,1,1,1,0],
            [1,0,0,0,0],
            [1,1,0,0,0],
            [1,1,1,1,1]], 
            k = 3
        ))
        self.assertEqual([0,2], caller(
            mat = 
            [[1,0,0,0],
            [1,1,1,1],
            [1,0,0,0],
            [1,0,0,0]], 
            k = 2
        ))

if __name__ == '__main__':
    unittest.main()