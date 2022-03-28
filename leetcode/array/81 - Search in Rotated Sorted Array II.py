
# Medium - 81 - Search in Rotated Sorted Array II

import unittest

class Solution:
    def search(self, nums, target: int) -> bool:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[right]: # Fail to estimate which side is sorted
                right -= 1
            elif nums[mid] > nums[right]: # Left side of mid is sorted
                if  nums[left] <= target and target < nums[mid]: # Target in the left side
                    right = mid - 1
                else: # in right side
                    left = mid + 1
            else: # Right side is sorted
                if  nums[mid] < target and target <= nums[right]: # Target in the right side
                    left = mid + 1
                else: # in left side
                    right = mid - 1
        return False
        

        
    
def caller(nums, target):
    sl = Solution()
    return sl.search(nums, target)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(True, caller(
            nums = [2,5,6,0,0,1,2], target = 0
        ))
        self.assertEqual(False, caller(
            nums = [2,5,6,0,0,1,2], target = 3
        ))

if __name__ == '__main__':
    unittest.main()