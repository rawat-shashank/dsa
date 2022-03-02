# Easy - 344 - Reverse String
import unittest

def firstTry(s):
    """
    Accpeted
    204ms | 18.4MB
    Two pointer approch and no extra space
    """
    i, n = 0, len(s)/2
    while i < n:
        s[i], s[-i-1] = s[-i-1], s[i]
        i+=1
    return s
    
def caller(s):
    return firstTry(s)

class Tests(unittest.TestCase):
    def tests(self):
        self.assertEqual(["o","l","l","e","h"], caller(
            s = ["h","e","l","l","o"]
        ))
        self.assertEqual(["h","a","n","n","a","H"], caller(
            s = ["H","a","n","n","a","h"]
        ))
        self.assertEqual(["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"], caller(
            s = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
        ))

if __name__ == '__main__':
    unittest.main()