# Easy - 977 - Squares of a Sorted Array

import unittest

class Solution:
    def sortedSquares(self, nums):
        l, r, res = 0, len(nums)-1, [0]*len(nums)
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[r-l] = pow(nums[l], 2)
                l+=1
            else:
                res[r-l] = pow(nums[r], 2)
                r-=1
        return res
                
    
def caller(nums):
    sl = Solution()
    return sl.sortedSquares(nums)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual([0,1,9,16,100], caller(
            nums = [-4,-1,0,3,10]
        ))
        self.assertEqual([4,9,9,49,121], caller(
            nums = [-7,-3,2,3,11]
        ))

if __name__ == '__main__':
    unittest.main()