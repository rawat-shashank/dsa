#Easy - 136 - Single Number

import unittest

def firstTry(nums):
    dp = {}
    sum = 0 
    for x in nums:
        if x in dp:
            sum -= x
        else:
            sum += x
            dp[x] = None
    return sum

def secondTry(nums):
    s = 0
    for x in nums:
        s ^= x
    return s

def caller(nums):
    return secondTry(nums)


class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(1, caller(
            nums = [2,2,1]
        ))
        self.assertEqual(4, caller(
            nums = [4,1,2,1,2]
        ))
        self.assertEqual(1, caller(
            nums = [1]
        ))

if __name__ == '__main__':
    unittest.main()