# Easy - 412 - Fizz Buzz

import unittest

class Solution:
    def fizzBuzz(self, n: int):
        ans = []
        for i in range(1, n+1):
            a = []
            if i % 3 == 0: a.append("Fizz")
            if i % 5 == 0: a.append("Buzz")
            ans.append("".join(a)) if len(a) else ans.append(str(i))
        return ans
            
    
def caller(n):
    sl = Solution()
    return sl.fizzBuzz(n)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(["1","2","Fizz"], caller(
            n = 3
        ))
        self.assertEqual(["1","2","Fizz","4","Buzz"], caller(
            n = 5
        ))
        self.assertEqual(["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"], caller(
            n=15
        ))

if __name__ == '__main__':
    unittest.main()