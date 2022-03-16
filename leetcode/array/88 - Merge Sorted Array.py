# Easy - 88 - Merge Sorted Array

import unittest

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        61ms | 13.9 MB
        """
        while m and n:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1
        if n > 0:
            nums1[:n] = nums2[:n]
        return nums1

    
def caller(nums1, m: int, nums2, n: int):
    sl = Solution()
    return sl.merge(nums1, m, nums2, n)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual([1,2,2,3,5,6], caller(
            nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        ))
        self.assertEqual([1], caller(
            nums1 = [1], m = 1, nums2 = [], n = 0
        ))
        self.assertEqual([1], caller(
            nums1 = [0], m = 0, nums2 = [1], n = 1
        ))
        self.assertEqual([1, 2], caller(
            nums1 = [2, 0], m = 1, nums2 = [1], n = 1
        ))

if __name__ == '__main__':
    unittest.main()