# Medium - 167 - Two Sum II - Input Array Is Sorted

import unittest
from math import sqrt

class Solution:
    def twoSum(self, numbers, target: int):
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum > target:
                right -= 1
            else:
                left += 1
        return -1
    
def caller(numbers, target):
    sl = Solution()
    return sl.twoSum(numbers, target)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual([1,2], caller(
            numbers = [2,7,11,15], target = 9
        ))
        self.assertEqual([1,3], caller(
            numbers = [2,3,4], target = 6
        ))
        self.assertEqual([1,2], caller(
            numbers = [-1,0], target = -1
        ))

if __name__ == '__main__':
    unittest.main()