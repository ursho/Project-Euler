import unittest
from problems.FibonacciGenerator import FibonacciGenerator


class TestFibonacciGenerator(unittest.TestCase):
    def test_Fibonacci(self):
        self.assertEqual(0, fibonacci(1))
        self.assertEqual(1, fibonacci(2))
        self.assertEqual(1, fibonacci(3))
        self.assertEqual(2, fibonacci(4))
        self.assertEqual(3, fibonacci(5))
        self.assertEqual(5, fibonacci(6))

    def test_nextFibonacci(self):
        fg = FibonacciGenerator()
        self.assertEqual(fibonacci(1), fg.next())
        self.assertEqual(fibonacci(2), fg.next())
        self.assertEqual(fibonacci(3), fg.next())
        self.assertEqual(fibonacci(4), fg.next())
        self.assertEqual(fibonacci(5), fg.next())
        self.assertEqual(fibonacci(6), fg.next())

    def test_fibonacciOverflow(self):
        with self.assertRaises(OverflowError):
            list(FibonacciGenerator())


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
