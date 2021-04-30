import unittest 
from book.ch02.SequenceIterator import SequenceIterator
from book.ch02.Range import Range

class Ch02Test(unittest.TestCase):

    def test_sequenceIterator_value(self):
        self.obj = SequenceIterator([1,2,3,4])
        self.assertEquals(1, next(self.obj))
        self.assertEquals(2, next(self.obj))
        self.assertEquals(3, next(self.obj))
        self.assertEquals(4, next(self.obj))
        self.assertRaises(StopIteration, next, self.obj)
    
    def test_range(self):
        self._obj = Range(2);
        self.assertEquals(0, self._obj[0])
        self.assertEquals(1, self._obj[1])
        self.assertRaises(IndexError, self._obj.__getitem__, 6)

if __name__ == '__main__': 
    unittest.main()