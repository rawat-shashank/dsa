# Medium - 204 - Count Primes

import unittest
from math import sqrt

class Solution:
    def countPrimes(self, n: int) -> int:        
        def isPrime(n: int) -> bool:
            m = int(sqrt(n))
            for i in range(2, m+1):
                if n % i == 0:
                    return False
            return True
        
        c = 0
        for i in range(2, n):
            if isPrime(i):
                c+=1
        return c
    
    def countPrimes1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == 1:
                s[i * i:n:i] = [0] * len(s[i * i:n:i])
        return sum(s)
    
def caller(n):
    sl = Solution()
    return sl.countPrimes1(n)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(4, caller(
            n = 10
        ))
        self.assertEqual(0, caller(
            n = 0
        ))
        self.assertEqual(0, caller(
            n=1
        ))
        self.assertEqual(0, caller(
            n=2
        ))

if __name__ == '__main__':
    unittest.main()