class FizzBuzz:
    FIZZ = 'Fizz'
    BUZZ = 'Buzz'

    def __init__(self):
        pass

    def fizz(self, user_number: int) -> str:
        if user_number % 3 == 0 and user_number != 0:
            return self.FIZZ
        return ''

    def buzz(self, user_number: int) -> str:
        if user_number % 5 == 0 and user_number != 0:
            return self.BUZZ
        return ''
