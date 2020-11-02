import unittest
from problems.Primes import least_common_multiple_of_numbers_up_to, least_common_multiple_of


class TestProblem0005(unittest.TestCase):
    def test_least_common_muliple(self):
        self.assertEqual(2520, least_common_multiple_of_numbers_up_to(10))
        self.assertEqual(232792560, least_common_multiple_of_numbers_up_to(20))
        self.assertEqual(48, least_common_multiple_of(6, 8, 12, 16, 24))


if __name__ == '__main__':
    unittest.main()
