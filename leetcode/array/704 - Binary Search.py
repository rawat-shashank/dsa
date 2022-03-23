# Easy - 704 - Binary Search

import unittest

class Solution:
    def search(self, nums, target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            print(mid, nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        return -1


    
def caller(nums, target):
    sl = Solution()
    return sl.search(nums, target)

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, caller(
            nums = [-1,0,3,5,9,12], target = 9
        ))
        self.assertEqual(-1, caller(
            nums = [-1,0,3,5,9,12], target = 2
        ))
        self.assertEqual(-1, caller(
            nums = [-1,0,3,5,9,12], target = 13
        ))

if __name__ == '__main__':
    unittest.main()