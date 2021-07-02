# Easy - 1 - Two Sum - Success
import unittest


def twoSum(nums, target: int):
    outDict = {}
    for idx, val in enumerate(nums):
        if val in outDict:
            return [outDict[val], idx]
        else:
            outDict[target - val] = idx
    return []


class TestTwoSum(unittest.TestCase):

    def test_missing_number(self):
        print("test two sum")
        self.assertEqual([1, 2], twoSum(nums=[3, 2, 4], target=6))
        self.assertEqual([0, 1], twoSum(nums=[2, 7, 11, 15], target=9))
        self.assertEqual([0, 1], twoSum(nums=[3, 3], target=6))


if __name__ == '__main__':
    unittest.main()
