import unittest
import problems.Problem0002


class TestProblem0002(unittest.TestCase):
    def test_nextFibonacci(self):
        problem = problems.Problem0002.Problem0002()
        self.assertEqual(fibonacci(1), problem.next_fibonacci())
        self.assertEqual(fibonacci(2), problem.next_fibonacci())
        self.assertEqual(fibonacci(3), problem.next_fibonacci())
        self.assertEqual(fibonacci(4), problem.next_fibonacci())
        self.assertEqual(fibonacci(5), problem.next_fibonacci())
        self.assertEqual(fibonacci(6), problem.next_fibonacci())

    def test_Fibonacci(self):
        self.assertEqual(0, fibonacci(1))
        self.assertEqual(1, fibonacci(2))
        self.assertEqual(1, fibonacci(3))
        self.assertEqual(2, fibonacci(4))
        self.assertEqual(3, fibonacci(5))
        self.assertEqual(5, fibonacci(6))

    def test_sumOfEvensUpTo0(self):
        self.assertEqual(0, problems.Problem0002.sum_of_evens_up_to(0))

    def test_sumOfEvensUpTo1(self):
        self.assertEqual(0, problems.Problem0002.sum_of_evens_up_to(1))

    def test_sumOfEvensUpTo2(self):
        self.assertEqual(2, problems.Problem0002.sum_of_evens_up_to(2))

    def test_sumOfEvensUpTo8(self):
        self.assertEqual(10, problems.Problem0002.sum_of_evens_up_to(8))

    def test_sumOfEvensUpTo33(self):
        self.assertEqual(10, problems.Problem0002.sum_of_evens_up_to(33))

    def test_sumOfEvensUpTo34(self):
        self.assertEqual(44, problems.Problem0002.sum_of_evens_up_to(34))

    def test_sumOfEvensUpTo143(self):
        self.assertEqual(44, problems.Problem0002.sum_of_evens_up_to(143))

    def test_sumOfEvensUpTo144(self):
        self.assertEqual(188, problems.Problem0002.sum_of_evens_up_to(144))

    def test_sumOfEvensUpTo4Million(self):
        self.assertEqual(4613732, problems.Problem0002.sum_of_evens_up_to(4 * 1000 * 1000))


def fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    unittest.main()
