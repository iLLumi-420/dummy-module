import unittest
from dummy.greet import greet_user

class GreetTestCase(unittest.TestCase):
    def test_greet_user(self):

        result = greet_user('John')
        self.assertEqual(result, 'Hello John')

        result = greet_user('  John  ')
        self.assertEqual(result, 'Hello John')

        result = greet_user('')
        self.assertEqual(result, 'Hello ')

        result = greet_user(None)
        self.assertCountEqual(result, 'Not a string value')

        result = greet_user(['John'])
        self.assertCountEqual(result, 'Not a string value')

    

if __name__ == '__main__':
    unittest.main()
