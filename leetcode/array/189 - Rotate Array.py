#Medium - 189 - Rotate Array

import unittest

def firstTry(nums, k):
    """
    time limit exceded
    rotate array right side k number of times
    here we read the array from reverse one by
    one and copy to next element. And at last 
    replace the element at 0 with temp value
    """
    for j in range(k):
        temp = nums[-1]
        for i in range(len(nums)-1, 0, -1):
            nums[i] = nums[i - 1 % len(nums)]
        nums[0] = temp
    return nums

def secondTry(nums, k):
    """
    Accepted,
    Using hint from the question.
    Here i am using python inbuilt array indices,
    first we need to normalise k if it's larger than length
    then using indices, we replace the array with
    new array which contains the second part and than first part of the
    array.
    """
    k = k%len(nums)
    nums[:] = nums[-k::] + nums[:-k:]
    return nums



def caller(nums, k):
    return secondTry(nums, k)


class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual([5,6,7,1,2,3,4], caller(
            nums = [1,2,3,4,5,6,7],
            k = 3
        ))
        self.assertEqual([3,99,-1,-100], caller(
            nums = [-1,-100,3,99], k = 2
        ))
        self.assertEqual([2,1], caller(
            nums = [1, 2], k = 3
        ))

if __name__ == '__main__':
    unittest.main()