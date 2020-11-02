import unittest

from problems.Primes import nth_prime

class TestProblem0007(unittest.TestCase):
    def test_1st_prime(self):
        self.assertEqual(2, nth_prime(1))

    def test_2nd_prime(self):
        self.assertEqual(3, nth_prime(2))

    def test_6th_prime(self):
        self.assertEqual(13, nth_prime(6))

    def test_10001st_prime(self):
            self.assertEqual(104743, nth_prime(10001))


if __name__ == '__main__':
    unittest.main()
