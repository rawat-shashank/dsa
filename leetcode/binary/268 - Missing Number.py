# Easy - 268 - Missing Number - Success

# intended solution with bit manipulation (XOR)
# def missing_number(nums) -> int:
#     m = len(nums)
#     for i, num in enumerate(nums):
#         m ^= i ^ num
#     return m

# faster solution with less memory
import unittest


def missing_number(nums) -> int:
    ars = ts = 0
    for i in range(0, len(nums)):
        ts, ars = ts+(i+1), ars+nums[i]
    return ts - ars


class TestMissingNumber(unittest.TestCase):

    def test_missing_number(self):
        print("test missing number")
        self.assertEqual(0, missing_number([1]))
        self.assertEqual(2, missing_number([3, 0, 1]))


if __name__ == '__main__':
    unittest.main()
