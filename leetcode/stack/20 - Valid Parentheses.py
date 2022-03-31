import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        """
        0800
        0811
        """
        a, d = [], { ')': '(', '}': '{', ']':'[' }
        for x in s:
            if x in d:
                if not a or d[x] is not a.pop():
                    return False
            else:
                a.append(x)
        return a==[]

def caller(s):
    sl = Solution()
    return sl.isValid(s)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(True, caller(
            s = "()"
        ))
        self.assertEqual(True, caller(
            s = "()[]{}"
        ))
        self.assertEqual(False, caller(
            s = "(]"
        ))

if __name__ == '__main__':
    unittest.main()