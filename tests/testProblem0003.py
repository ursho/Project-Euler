import unittest
from problems.Problem0003 import prime_factors_of


class TestProblem0003(unittest.TestCase):
    def test_prime_factors_of_3(self):
        p = prime_factors_of(3)
        self.assertListEqual([3],p)

    def test_prime_factors_of_6(self):
        p = prime_factors_of(6)
        self.assertListEqual([2,3],p)

    def test_greatest_prime_factor_of_600851475143(self):
        p = prime_factors_of(600851475143)
        print(p)
        self.assertEqual(6857, p[-1])

if __name__ == '__main__':
    unittest.main()
