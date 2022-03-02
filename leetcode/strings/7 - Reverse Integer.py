# Medium - 7 - Reverse Integer
import unittest

def firstTry(x):
    """
    Accpeted
    70 ms, faster than 6.94% of Python3
    13.9 MB, less than 55.29% of Python3
    """
    n, sign = 0, 1
    if x < 0:
        sign = -1
        x = abs(x)
    while x > 0:
        r = x % 10
        x = x // 10
        n = (n*10) + r
    return 0 if n > 2147483648 else n * sign
    
def caller(x):
    return firstTry(x)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(321, caller(
            x = 123
        ))
        self.assertEqual(-321, caller(
            x = -123
        ))
        self.assertEqual(21, caller(
            x = 120
        ))
        self.assertEqual(0, caller(
            x = 1534236469
        ))

if __name__ == '__main__':
    unittest.main()