import unittest

from dummy import calculations

class CalculationsTestCase(unittest.TestCase):

    def testCalculations(self):

        result = calculations.addition(2,3)
        self.assertEqual(result, 5)

        result = calculations.subtraction(2,3)
        self.assertEqual(result, -1)

        result = calculations.multiplication(2,3)
        self.assertEqual(result, 6)

        result = calculations.division(2,3)
        self.assertEqual(result, 2/3)

if __name__ == '__main__':
    unittest.main()