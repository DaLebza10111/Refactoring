def fizzBuzz(number):

    if isinstance(number, int):

        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
            return

        if number % 3 != 0 and number % 5 != 0:
            print(number)
            return

        if number % 3 == 0:
            print("Fizz")
            return

        if number % 5 == 0:
            print("Buzz")
            return
    else:
        print("Input is not an integer.")
        return


if __name__ == "__main__":
    fizzBuzz(15)