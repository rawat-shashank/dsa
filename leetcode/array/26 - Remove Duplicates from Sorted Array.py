#Easy - 26 - Remove Duplicates from Sorted Array

import unittest

def firstTry(nums):
    """
    Accepted
    Here i tried using two pointer from 0 and 1 namely n and m
    if n and m position elements are duplicate, we continue
    else we replace pos n elements with pos m elements and move n
    pointer one step ahead, which keeps track of only unique
    elements
    """
    n=0
    for m in range(1, len(nums)):
        if nums[n] != nums[m]:
            nums[n+1] = nums[m]
            n+=1
    return n+1


def caller(nums):
    return firstTry(nums)


class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(2, caller(
            nums=[1,1,2]
        ))
        self.assertEqual(5, caller(
            nums=[0,0,1,1,1,2,2,3,3,4]
        ))

if __name__ == '__main__':
    unittest.main()
