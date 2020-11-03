import unittest
from math import prod


def pythagorean_tuple_for_sum(number):
    for a in range(3, (number - 3) // 3):
        for b in range(a + 1, (number - a) // 2):
            c = number - a - b
            if c ** 2 == a ** 2 + b ** 2:
                return a, b, c
    return 0


class TestProblem0009(unittest.TestCase):
    def test_pythagorean_tuple_for_sum(self):
        self.assertEqual(31875000, prod(pythagorean_tuple_for_sum(1000)))


if __name__ == '__main__':
    unittest.main()
