import pytest
from FizzBuzz import FizzBuzz


@pytest.fixture()
def fizz_buzz_class():
    return FizzBuzz()


def test_return_empty_string(fizz_buzz_class):
    assert fizz_buzz_class.fizz(0) == ''


@pytest.mark.parametrize("test_input,expected", [(3, 'Fizz'), (6, 'Fizz'), (9, 'Fizz')])
def test_return_fizz(fizz_buzz_class, test_input, expected):
    assert fizz_buzz_class.fizz(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(5, 'Buzz'), (10, 'Buzz'), (15, 'Buzz')])
def test_return_buzz(fizz_buzz_class, test_input, expected):
    assert fizz_buzz_class.buzz(test_input) == expected


if __name__ == '__main__':
    pytest.main()
