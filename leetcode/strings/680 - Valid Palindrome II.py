import unittest

class Solution:
    def isPalindrome(self, s:str) -> bool:
        i, j = 0, len(s) - 1
        while(i < j):
            if(s[i] != s[j]):
                return False
            else:
                i += 1
                j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        """
        1130
        1149
        """
        i, j = 0, len(s) - 1
        while(i < j):
            if(s[i] != s[j]):
                opt1 = self.isPalindrome(s[i:j])
                opt2 = self.isPalindrome(s[i+1:j+1])
                return opt1 or opt2
            i += 1
            j -= 1
        return True


def caller(s):
    so = Solution()
    return so.validPalindrome(s)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(True, caller(
            s = "aba"
        ))
        self.assertEqual(True, caller(
            s = "abca"
        ))
        self.assertEqual(False, caller(
            s = "abc"
        ))

if __name__ == '__main__':
    unittest.main()