import unittest
from problems.Problem0004 import palindrome_of_3, find_greatest_palindrome


class TestProblem0004(unittest.TestCase):
    def test_palinedrome_of_3(self):
        self.assertEqual(123321, palindrome_of_3(123))
        self.assertEqual(100001, palindrome_of_3(100))

    def test_factors(self):
        self.assertEqual(906609, find_greatest_palindrome())


if __name__ == '__main__':
    unittest.main()
