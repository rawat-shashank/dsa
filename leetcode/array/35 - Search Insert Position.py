# Easy - 35 - Search Insert Position

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
        return mid + 1 if target > nums[mid] else mid

    
def caller(nums, target):
    sl = Solution()
    return sl.search(nums, target)

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, caller(
            nums = [1,3,5,6], target = 5
        ))
        self.assertEqual(1, caller(
            nums = [1,3,5,6], target = 2
        ))
        self.assertEqual(4, caller(
            nums = [1,3,5,6], target = 7
        ))
        self.assertEqual(0, caller(
            nums = [1,3,5,6], target = 0
        ))

if __name__ == '__main__':
    unittest.main()