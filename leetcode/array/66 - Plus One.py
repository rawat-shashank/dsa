#Easy - 66 - Plus One

import unittest

def firstTry(digits):
    """
    Accepted
    54ms | 13.9 MB
    """
    num = str(
        int(''.join([str(x) for x in digits])) + 1
    )
    return [int(x) for x in num]

def secondTry(digits):
    """
    Accepted
    32ms | 13.9 MB
    """
    for i in range(len(digits) - 1,-1,-1):
        if digits[i] < 9:
            digits[i] +=1
            return digits
        else:
            digits[i] = 0
    digits.insert(0, 1)
    return digits


def caller(digits):
    return secondTry(digits)


class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual([1,2,4], caller(
            digits = [1,2,3]
        ))
        self.assertTrue([4,3,2,2], caller(
            digits = [4,3,2,1]
        ))
        self.assertTrue([1,0], caller(
            digits = [9]
        ))

if __name__ == '__main__':
    unittest.main()