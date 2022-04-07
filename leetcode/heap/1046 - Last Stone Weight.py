import unittest
from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        1350
        1357
        """
        stones = [-x for x in stones]
        heapify(stones)
        while len(stones) > 1:
            s1, s2 = heappop(stones), heappop(stones)
            if s1 != s2: heappush(stones, s1 - s2)
        return 0 if len(stones) == 0 else -heappop(stones)


def caller(stones):
    sl = Solution()
    return sl.lastStoneWeight(stones)


class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(1, caller(
            stones=[2, 7, 4, 1, 8, 1]
        ))
        self.assertEqual(1, caller(
            stones=[1]
        ))
        self.assertEqual(0, caller(
            stones=[1, 1]
        ))


if __name__ == '__main__':
    unittest.main()
