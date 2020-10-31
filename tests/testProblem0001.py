import unittest
from problems.Problem0001 import sum


class TestProblem0001(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(233168, sum(3, 5, 1000))


if __name__ == '__main__':
    unittest.main()
