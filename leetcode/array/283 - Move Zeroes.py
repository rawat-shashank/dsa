#Easy - 283 - Move Zeroes

import unittest

def firstTry(nums):
  """
  Accepted
  263 ms | 15.5 MB
  """
  i,j = 0, 1
  while j < len(nums):
      if nums[j] != 0 and nums[i] == 0:
          nums[i], nums[j] = nums[j], nums[i]
      if nums[i] != 0:
          i += 1
      j+=1
  return nums

def caller(nums):
    return firstTry(nums)


class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual([1,3,12,0,0], caller(
            nums = [0,1,0,3,12]
        ))
        self.assertEqual([0], caller(
            nums = [0]
        ))
        self.assertEqual([1, 0], caller(
            nums = [0, 1]
        ))
        self.assertEqual([2, 1], caller(
            nums = [2, 1]
        ))
        self.assertEqual([4,2,4,3,5,1,0,0,0,0], caller(
            nums = [4,2,4,0,0,3,0,5,1,0]
        ))

if __name__ == '__main__':
    unittest.main()