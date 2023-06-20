import unittest
from dummy.greet import greet_user

class GreetTestCase(unittest.TestCase):
    def test_greet_user(self):
        result = greet_user('John')
        self.assertEqual(result, 'Hello John')

        result = greet_user('  John  ')
        self.assertEqual(result, 'Hello John')

    

if __name__ == '__main__':
    unittest.main()
