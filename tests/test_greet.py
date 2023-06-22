import pytest
from dummy.greet import greet_user

@pytest.mark.parametrize("greet , expected_output",[
    ('John', 'Hello John'),
    ('  John  ', 'Hello John'),
    ('', 'Hello ' ),
    (None, 'Not a string value'),
    ([], 'Not a string value'),
    ({}, 'Not a string value'),

])
def test_greet_user(greet, expected_output):
    assert greet_user(greet) == expected_output


if __name__ == '__main__':
    print('Running greet test directly')
    pytest.main([__file__])
    
