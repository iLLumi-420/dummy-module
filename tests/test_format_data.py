import pytest

from dummy.format_data import format_data_for_display, format_data_for_excel

@pytest.fixture
def people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

def test_formaT_data_for_display(people_data):
    assert format_data_for_display(people_data) == [
        'Alfonsa Ruiz: Senior Software Engineer',
        'Sayid Khan: Project Manager'
    ]

def test_format_data_for_excel(people_data):
    assert format_data_for_excel(people_data) == 'given,family,title\nAlfonsa,Ruiz,Senior Software Engineer\nSayid,Khan,Project Manager\n'


if __name__ == '__main__':
    print('Running format_display test directly')
    pytest.main([__file__])