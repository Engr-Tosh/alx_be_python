#testing the simple calculator script, to ensur proper functionality

#import the necessary modules
import unittest
from simple_calculator import SimpleCalculator

#define a test class
class TestSimpleCalculator(unittest.TestCase):
    #set a setup and teardown, so variables inputted before each test begins.

    def setUp(self):
        #Set up the simple calculator before each test
        self.calc = SimpleCalculator()
                
    #write test methods
    def test_add(self):
        self.assertEqual(self.calc.add(3, 3), 6)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)
        self.assertEqual(self.calc.multiply(-3, 2), -6)
        self.assertEqual(self.calc.multiply(3, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(6, 0), None)

    
        

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)
