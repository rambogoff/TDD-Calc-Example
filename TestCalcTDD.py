import Calc
import unittest


class TestHesap(unittest.TestCase):

    def setUp(self):
        self.calc = Calc.Calc()

    def test_addition(self):
        result = self.calc.addition(5,6)
        self.assertEqual(11, result)

    def test_add_value(self):
        self.assertRaises(ValueError, self.calc.addition, "five", "six")

    def test_subtraction(self):
        result = self.calc.subtraction(7, 6)
        self.assertEqual(1, result)

    def test_sub_value(self):
        self.assertRaises(ValueError, self.calc.subtraction, "eight", "six")

    def test_multiply(self):
        result = self.calc.multiply(4, 5)
        self.assertEqual(20, result)

    def test_multiply_value(self):
        self.assertRaises(ValueError, self.calc.multiply, "five", "two")

    def test_division(self):
        result = self.calc.division(6, 2)
        self.assertEqual(3, result)

    def test_division_zero(self):
        self.assertRaises(ZeroDivisionError, self.calc.division, 6, 0)

    def test_division_value(self):
        self.assertRaises(ValueError, self.calc.division, "five", "two")
if __name__=="__main__":
    unittest.main()