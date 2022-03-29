import unittest
from math import sqrt
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        rows, cols = len(matrix), len(matrix[0])
        begin, end = 0, rows * cols - 1
        while begin <= end:
            mid = (begin + end) // 2
            num = matrix[mid//cols][mid%cols]
            if num == target: return True
            elif num < target: begin = mid + 1
            else: end = mid - 1
        return False
            
    
def caller(matrix, target):
    sl = Solution()
    return sl.searchMatrix(matrix, target)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(True, caller(
            matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
        ))
        self.assertEqual(False, caller(
            matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
        ))

if __name__ == '__main__':
    unittest.main()