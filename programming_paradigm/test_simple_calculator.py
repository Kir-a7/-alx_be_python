import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        add = self.calc.add
        self.assertEqual(add(2,3), 5)
    
    def test_subtraction(self):
        sub = self.calc.subtract
        self.assertEqual(sub(4-1), 3)

    def test_division(self):
        div = self.calc.divide
        self.assertEqual(div(6, 3), 2)
        self.assertIsNone(div(1, 0))
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        
        
