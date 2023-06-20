import unittest

from dummy.calculations import sum

class CalculationTestCase(unittest.TestCase):

    def test_sum(self):

        result = sum(2, 3)
        self.assertEqual(result, 5)

        result = sum(2, None)
        self.assertEqual(result, 'Provide int or float values')


if __name__ == '__main__':
    unittest.main()