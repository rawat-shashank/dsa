# Easy - 953 - Verifying an Alien Dictionary

import unittest

def firstTry(words, order):
    """
        Accepted
        First loop through all the words with there adjcent word.
        In every loop trying to find any negative condition that
        will break the flow with return False
        condition 1 : if len of first word is greater than second,
            while all char before the current one are 
    """
    for i in range(0, len(words)-1, 1):
        for j in range(max(
            len(words[i]), 
            len(words[i+1])
        )):            
            try:
                words[i][j]
            except IndexError:
                break
            try:
                words[i+1][j]
            except IndexError:
                return False
            
            if order.index(words[i][j]) > order.index(words[i+1][j]):
                return False
            elif order.index(words[i][j]) < order.index(words[i+1][j]):
                break
            else:
                continue
    return True


def caller(words, order):
    return firstTry(words, order)


class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(True, caller(
            words = ["hello","leetcode"],
            order = "hlabcdefgijkmnopqrstuvwxyz"
        ))
        self.assertEqual(False, caller(
            words = ["word","world","row"],
            order = "worldabcefghijkmnpqstuvxyz"
        ))
        self.assertEqual(False, caller(
            words = ["apple","app"],
            order = "abcdefghijklmnopqrstuvwxyz"
        ))
        self.assertEqual(True, caller(
            words = ["app","apple"],
            order = "abcdefghijklmnopqrstuvwxyz"
        ))
        self.assertEqual(False, caller(
            words = ["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"],
            order = "zkgwaverfimqxbnctdplsjyohu"
        ))

if __name__ == '__main__':
    unittest.main()
