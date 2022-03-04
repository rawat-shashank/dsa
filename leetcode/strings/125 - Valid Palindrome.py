
# Easy - 125 - Valid Palindrome

from curses.ascii import isalpha
import unittest

def firstTry(s):
    """
    Accpeted
    81ms | 14.4MB
    """
    i, j = 0, len(s)-1
    while (i <= j):
        if not s[i].isalnum():
            i+=1
            continue
        if not s[j].isalnum():
            j-=1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i+=1
        j-=1
    return True

    
def caller(s):
    return firstTry(s)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(True, caller(
            s = "A man, a plan, a canal: Panama"
        ))
        self.assertEqual(False, caller(
            s = "race a car"
        ))
        self.assertEqual(True, caller(
            s = " "
        ))
        self.assertEqual(False, caller(
            s = "0P"
        ))

if __name__ == '__main__':
    unittest.main()