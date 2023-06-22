import pytest

from dummy.char_position import char_position

@pytest.mark.parametrize('text , expected_output ', [
    ('Hello', {'H': {0}, 'e': {1}, 'l':{2,3}, 'o':{4}}),
    ('abc', {'a': {0}, 'b': {1}, 'c':{2}}),
    ('Sandeep',{'S': {0}, 'a': {1}, 'n':{2}, 'd':{3}, 'e':{4,5}, 'p': {6} }),
    ( ['sbc'], 'Please input string' )
])
def test_char_position(text, expected_output):
    assert char_position(text) == expected_output

if __name__ == '__main__':
    print('Running Char_Posotion test directly')
    pytest.main([__file__])

