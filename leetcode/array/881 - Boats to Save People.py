# Medium - 881 - Boats to Save People

import unittest

class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        left, right, ans = 0, len(people) - 1, 0
        people = sorted(people)
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            ans+=1
        return ans
        
def caller(people, limit):
    sl = Solution()
    return sl.numRescueBoats(people, limit)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(1, caller(
            people = [1,2], limit = 3
        ))
        self.assertEqual(3, caller(
            people = [3,2,2,1], limit = 3
        ))
        self.assertEqual(4, caller(
            people = [3,5,3,4], limit = 5
        ))

if __name__ == '__main__':
    unittest.main()