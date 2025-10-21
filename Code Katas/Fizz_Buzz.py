def fizzBuzz(number):

    if isinstance(number, int):

        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")

        elif number % 3 != 0 and number % 5 != 0:
            print(number)

        elif number % 3 == 0:
            print("Fizz")

        elif number % 5 == 0:
            print("Buzz")

    else:
        print("Input is not an integer.")
