# Medium - 1029 - Two City Scheduling

import unittest
from math import sqrt

class Solution:
    def twoCitySchedCost(self, costs) -> int:
        """
        0715
        """
        costFirstCity = [i for i, _ in costs]
        costDiff = [j - i for i,j in costs]
        return sum(costFirstCity) + sum(
            sorted(costDiff)[:len(costs)//2]
        )
    
def caller(costs):
    sl = Solution()
    return sl.twoCitySchedCost(costs)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(110, caller(
            costs = [[10,20],[30,200],[400,50],[30,20]]
        ))
        self.assertEqual(1859, caller(
            costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
        ))
        self.assertEqual(3086, caller(
            costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
        ))

if __name__ == '__main__':
    unittest.main()