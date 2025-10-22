def fizzBuzz(number):

    if isinstance(number, int):

        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"

        elif number % 3 != 0 and number % 5 != 0:
            return number

        elif number % 3 == 0:
            return "Fizz"

        elif number % 5 == 0:
            return "Buzz"

    else:
        return "Input is not an integer."
