
class R1Questions:
    
    def is_multiple(self,n,m):
        """ r1.1 """
        return True if m % n == 0 else False

    def is_even(self, n):
        """ r1.2 """
        return False if n & 1 else True
    
    def minmaxSeq(self, seq):
        """ r1.3 """
        # not optimized for strings
        minVal, maxVal = seq[0], seq[0]
        for val in seq:
            if val < minVal:
                minVal = val
            if val > maxVal:
                maxVal = val
        return minVal, maxVal
    
    def squareSum(self, n):
        """ r1.4 and r1.5 sum of square of all postive interger smaller than n """
        return sum([i*i for i in range(1, n-1)])
    
    def squareSumOdd(self, n):
        """ r1.6 and r1.7 sum of square of all odd postive interger smaller than n """
        return sum([i*i for i in range(1, n-1) if i % 2!=0])