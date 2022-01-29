# Easy - 1920 - Build Array from Permutation - Accepted

import unittest

def firstTry(nums):
    resp = []
    for i, x in enumerate(nums):
        resp.append(nums[nums[i]])
    return resp

def secondTry(nums):
    return  [nums[x] for x in nums]

class Testcases(unittest.TestCase):

    def test_nums(self):
        self.assertEqual([0,1,2,4,5,3], secondTry([0,2,1,5,3,4]))
        self.assertEqual([4,5,0,1,2,3], secondTry([5,0,1,2,3,4]))

if __name__ == '__main__':
    unittest.main()
