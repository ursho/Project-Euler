import unittest
from problems.Problem0004 import is_palindrome, find_greatest_palindrome


class TestProblem0004(unittest.TestCase):
    def test_is_palindrome(self):
        palindromes = set(map(lambda x: palindrome_of_3(x), range(100, 1000)))
        for i in range(100000, 1000000):
            self.assertEqual(is_palindrome(i), i in palindromes)

    def test_find_greatest_palindrome(self):
        self.assertEqual(906609, find_greatest_palindrome())


def palindrome_of_3(half):
    return ((half * 10 + half % 10) * 10 + half // 10 % 10) * 10 + half // 100


if __name__ == '__main__':
    unittest.main()
