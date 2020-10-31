import unittest
import problems.Problem0001


class TestProblem0001(unittest.TestCase):
    def test_sum(self):
        problem = problems.Problem0001
        self.assertEqual(233168, problem.sum(3, 5, 1000))


if __name__ == '__main__':
    unittest.main()
