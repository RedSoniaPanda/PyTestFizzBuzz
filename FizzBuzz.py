import re


class FizzBuzz:
    FIZZ = 'Fizz'
    BUZZ = 'Buzz'
    EMPTY_STRING = ''

    def __init__(self):
        pass

    def fizz(self, user_number: int) -> str:
        if user_number % 3 == 0 and user_number != 0:
            return self.FIZZ
        return self.EMPTY_STRING

    def buzz(self, user_number: int) -> str:
        if user_number % 5 == 0 and user_number != 0:
            return self.BUZZ
        return self.EMPTY_STRING

    def fizz_buzz(self, user_number: str) -> str:
        if re.match(r'\d*', user_number):
            user_number = int(user_number)
            return_string = self.fizz(user_number)
            return_string += self.buzz(user_number)
            return return_string

        return self.EMPTY_STRING
