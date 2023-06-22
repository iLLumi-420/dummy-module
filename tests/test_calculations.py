from dummy.calculations import sum
import pytest

def test_sum():

    assert sum(2, 3) == 5

    assert sum(2.0 , 3.0) == 5.0

    assert sum(2, [5,2]) == 'Provide int or float values'

if __name__ == '__main__':
    print('Running sum test directly')
    pytest.main([__file__])





