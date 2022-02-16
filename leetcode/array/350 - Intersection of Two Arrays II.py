#Easy - 350 - Intersection of Two Arrays II

import unittest

def firstTry(nums1, nums2):
    dp1, dp2 = {}, {}
    for x in nums1:
        dp1[x] = dp1.get(x, 0) + 1
        
    for x in nums2:
        dp2[x] = dp2.get(x, 0) + 1
    
    ans = []
    for x in dp1.keys():
        dp1[x] = min(dp1[x], dp2.get(x, 0))
        while dp1[x]:
            ans.append(x)
            dp1[x] -=1
    return ans

def secondTry(nums1, nums2):
    dp1= {}
    ans = []
    for x in nums1:
        dp1[x] = dp1.get(x, 0) + 1
    for x in nums2:
        if dp1.get(x, 0):
            dp1[x] -=1
            ans.append(x)
    return ans


def caller(nums1, nums2):
    return secondTry(nums1, nums2)


class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual([2,2], caller(
            nums1 = [1,2,2,1],
            nums2 = [2,2]
        ))
        self.assertTrue([4,9] or [9,4], caller(
            nums1 = [4,9,5],
            nums2 = [9,4,9,8,4]
        ))

if __name__ == '__main__':
    unittest.main()