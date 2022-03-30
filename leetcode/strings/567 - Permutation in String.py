import unittest
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts, w, matched = Counter(s1), len(s1), 0   

        for i in range(len(s2)):
            if s2[i] in counts: 
                counts[s2[i]] -= 1
                if counts[s2[i]] == 0:
                    matched += 1
            if i >= w and s2[i-w] in counts: 
                if counts[s2[i-w]] == 0:
                    matched -= 1
                counts[s2[i-w]] += 1

            if matched == len(counts):
                return True

        return False

def caller(s1, s2):
    sl = Solution()
    return sl.checkInclusion(s1, s2)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(True, caller(
            s1 = "ab", s2 = "eidbaooo"
        ))
        self.assertEqual(False, caller(
            s1 = "ab", s2 = "eidboaoo"
        ))

if __name__ == '__main__':
    unittest.main()