# Easy - 28 - Implement strStr()

import unittest

def firstTry(haystack, needle):
    """
    Accpeted
    72ms | 14MB
    """
    if not needle: return 0
    if not haystack: return -1
    hl, nl = len(haystack), len(needle)
    for i in range(0, hl):
        if haystack[i: i+nl] == needle : return i
    return -1
        

    

def caller(haystack, needle):
    return firstTry(haystack, needle)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(2, caller(
            haystack = "hello", needle = "ll"
        ))
        self.assertEqual(-1, caller(
            haystack = "aaaaa", needle = "bba"
        ))
        self.assertEqual(0, caller(
            haystack = "", needle = ""
        ))
        self.assertEqual(1, caller(
            haystack = "mississippi", needle = "issi"
        ))

if __name__ == '__main__':
    unittest.main()