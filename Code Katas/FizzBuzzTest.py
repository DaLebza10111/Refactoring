import unittest

from Fizz_Buzz import fizzBuzz


class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz_divisible_by_3_and_5(self):
        self.assertEqual(fizzBuzz(15), "FizzBuzz")

    def test_fizzbuzz_divisible_by_3(self):
        self.assertEqual(fizzBuzz(9), "Fizz")

    def test_fizzbuzz_divisible_by_5(self):
        self.assertEqual(fizzBuzz(10), "Buzz")

    def test_fizzbuzz_not_divisible_by_3_or_5(self):
        self.assertEqual(fizzBuzz(7), 7)

    def test_fizzbuzz_non_integer_input(self):
        self.assertEqual(fizzBuzz("hello"), "Input is not an integer.")
        self.assertEqual(fizzBuzz(3.5), "Input is not an integer.")


if __name__ == '__main__':
    unittest.main()