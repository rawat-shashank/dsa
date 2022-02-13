#Medium - Best Time to Buy and Sell Stock II

import unittest

def firstTry(prices):
    """
    Accepted
    to maximise the profit, we need to sum up all the positive
    difference. Here, I am check if the difference is postive. Adding
    the positive difference will give the desired result.
    """
    p = 0    
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            p += prices[i] - prices[i-1]
    return p

def secondTry(prices):
    """
    Accepted
    This is similiar to first try, here comparions are reduced
    by caluclating and storing it into another var.
    """
    p = 0    
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i-1]
        p += diff if diff > 0 else 0
    return p

def caller(prices):
    return firstTry(prices)


class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(7, caller(
            prices = [7,1,5,3,6,4]
        ))
        self.assertEqual(4, caller(
            [1,2,3,4,5]
        ))
        self.assertEqual(0, caller(
            prices = [7,6,4,3,1]
        ))

if __name__ == '__main__':
    unittest.main()