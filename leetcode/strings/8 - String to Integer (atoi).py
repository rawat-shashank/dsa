# Medium - 8 - String to Integer (atoi)

import unittest

def firstTry(s):
    """
    Accpeted
    61 ms | 14MB
    """
    if len(s) == 0 : return 0
    ls = list(s.strip())
    sign = -1 if ls[0] == '-' else 1
    if ls[0] in ['-','+'] : del ls[0]
    i, res = 0, []
    while i < len(ls) and ls[i].isdigit() :
        res.append(ls[i])
        i+=1
    num = sign * int(float(
        "".join(res) if len(res) else 0
    ))
    if num > 2147483647:
        return 2147483647
    elif num < -2147483648:
        return -2147483648
    else:
        return num

def caller(s):
    return firstTry(s)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(42, caller(
            s = "42"
        ))
        self.assertEqual(-42, caller(
            s = "   -42"
        ))
        self.assertEqual(4193, caller(
            s = "4193 with words"
        ))
        self.assertEqual(-2147483648, caller(
            s = "-91283472332"
        ))
        self.assertEqual(3, caller(
            s = "3.14159"
        ))
        self.assertEqual(0, caller(
            s = "+-12"
        ))

if __name__ == '__main__':
    unittest.main()