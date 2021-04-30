import unittest 
from book.ch01.r1 import R1Questions

class R1Test(unittest.TestCase):
    
    def setUp(self): 
        self.obj = R1Questions()

    def test_is_multiple(self):
        self.assertTrue(self.obj.is_multiple(2, 6))
        self.assertTrue(self.obj.is_multiple(3, 6))
        self.assertTrue(self.obj.is_multiple(2, 4))
        self.assertFalse(self.obj.is_multiple(3, 7))

    def test_is_even(self):
        self.assertFalse(self.obj.is_even(123))
        self.assertFalse(self.obj.is_even(3))
        self.assertTrue(self.obj.is_even(44))
        self.assertTrue(self.obj.is_even(78))

    def test_minmax(self):
        self.assertEqual( (1, 4) , self.obj.minmaxSeq([1, 2, 3, 4]))        # test for list
        self.assertEqual( (-2, 4) , self.obj.minmaxSeq([1, -2, 0, 4]))       # test for list and negative number
        self.assertEqual( (1, 4) , self.obj.minmaxSeq((1, 2, 3, 4)))        # test for tuple

    def test_squareSum(self):
        self.assertEquals(14, self.obj.squareSum(5))
        self.assertEquals(30, self.obj.squareSum(6))
    
    def test_squareSumOdd(self):
        self.assertEquals(10, self.obj.squareSumOdd(5))
        self.assertEquals(10, self.obj.squareSumOdd(6))
        self.assertEquals(35, self.obj.squareSumOdd(7))

if __name__ == '__main__': 
    unittest.main()