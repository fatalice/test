import unittest
#test
def divid(num1, num2):
    return num1/num2

#test
class MyTest(unittest.TestCase):
    def test1(self):
        assert(divid(1, 1)==1)
        
    def test2(self):
        assert(divid(0, 1)==0)

if __name__=="__main__":
    unittest.main()
