import pytest
from FizzBuzz import FizzBuzz


@pytest.fixture()
def fizz_buzz_class():
    return FizzBuzz()


@pytest.mark.parametrize("test_input,expected", [('5', 'Buzz'), ('3', 'Fizz'), ('15', 'FizzBuzz'), ('2', '')])
def test_return_fizz_buzz(fizz_buzz_class, test_input, expected):
    assert fizz_buzz_class.fizz_buzz(test_input) == expected


if __name__ == '__main__':
    pytest.main()
