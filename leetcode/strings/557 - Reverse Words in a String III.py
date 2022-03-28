# Easy - 557 - Reverse Words in a String III

import unittest

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x[::-1] for x in s.split(' ')])
    
def caller(s):
    sl = Solution()
    return sl.reverseWords(s)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual("s'teL ekat edoCteeL tsetnoc", caller(
            s = "Let's take LeetCode contest"
        ))
        self.assertEqual("doG gniD", caller(
            s = "God Ding"
        ))

if __name__ == '__main__':
    unittest.main()