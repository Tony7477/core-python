import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        #result=calc.add(10,5)
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(6,7),13)
        self.assertEqual(calc.add(8,7),15)
    def test_mult(self):
        #result=calc.add(10,5)
        self.assertEqual(calc.mult(10,5),50)
        self.assertEqual(calc.mult(6,7),42)
        self.assertEqual(calc.mult(8,7),56)
    
    def test_div(self):
        #result=calc.add(10,5)
        self.assertEqual(calc.div(10,5),2)
        self.assertEqual(calc.div(6,2),3)
        self.assertEqual(calc.div(8,4),2)
        #self.assertEqual(ValueError,calc.div,2,0)
        #similarily with context manager
        with self.assertRaises(ValueError):
            calc.div(2,0)
    
    def test_subt(self):
        #result=calc.add(10,5)
        self.assertEqual(calc.subt(10,5),5)
        self.assertEqual(calc.subt(6,7),-1)
        self.assertEqual(calc.subt(8,7),1)



if __name__=='__main__':
    unittest.main()


