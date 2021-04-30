import unittest
from book.ch05.examples import SeqExamples

class SeqExamplesTest(unittest.TestCase):

    def setUp(self):
        self.obj = SeqExamples()
    
    def test_insertion_sort(self):
        self.assertEqual([1,2,3,4], self.obj.insertion_sort([1,4,3,2]))
        self.assertEqual([1,2,3,4], self.obj.insertion_sort([4,2,3,1]))
        self.assertEqual([1,2,3,4], self.obj.insertion_sort([2,3,1,4]))
        self.assertEqual([1,2,3,4], self.obj.insertion_sort([3,2,4,1]))

if __name__ == '__main__': 
    unittest.main()