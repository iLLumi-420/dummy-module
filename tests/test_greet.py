from dummy.greet import greet_user

def test_greet_user():

    expected_output = 'Hello John'
    assert greet_user('John') == expected_output

    expected_output = 'Hello John'
    assert greet_user('   John   ') == expected_output

    expected_output = 'Hello '
    assert greet_user('') == expected_output

    expected_output = 'Not a string value'
    assert greet_user(None) == expected_output

    expected_output = 'Not a string value'
    assert greet_user(['John', 'Mary']) == expected_output


# class GreetTestCase(unittest.TestCase):
#     def test_greet_user(self):

#         result = greet_user('John')
#         self.assertEqual(result, 'Hello John')

#         result = greet_user('  John  ')
#         self.assertEqual(result, 'Hello John')

#         result = greet_user('')
#         self.assertEqual(result, 'Hello ')

#         result = greet_user(None)
#         self.assertCountEqual(result, 'Not a string value')

#         result = greet_user(['John'])
#         self.assertCountEqual(result, 'Not a string value')

