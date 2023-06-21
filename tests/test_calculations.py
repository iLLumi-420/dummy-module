from dummy.calculations import sum


def test_sum():

    assert sum(2, 3) == 5

    assert sum(2.0 , 3.0) == 5.0

    assert sum(2, [5,2]) == 'Provide int or float values'





