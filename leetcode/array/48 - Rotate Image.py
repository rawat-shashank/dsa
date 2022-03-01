#Medium - 36 - Rotate Image

import unittest

def firstTry(matrix):
    """
    Accpeted
    50ms | 13.9MB
    """
    n = len(matrix)
    i = 0
    while i < n/2:
        matrix[i], matrix[-i-1] = matrix[-i-1], matrix[i]
        i+=1
         
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    return matrix

def caller(matrix):
  return firstTry(matrix)

class Tests(unittest.TestCase):
    def tests(self):
      self.assertEqual([[7,4,1],[8,5,2],[9,6,3]], caller(
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
      ))
      self.assertEqual([[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]], caller(
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
      ))

if __name__ == '__main__':
    unittest.main()
