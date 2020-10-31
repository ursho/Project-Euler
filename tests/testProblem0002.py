import unittest
from problems.Problem0002 import sum_of_even_fibonaccis_up_to


class TestProblem0002(unittest.TestCase):
    def test_sumOfEvensUpTo0(self):
        self.assertEqual(0, sum_of_even_fibonaccis_up_to(0))

    def test_sumOfEvensUpTo1(self):
        self.assertEqual(0, sum_of_even_fibonaccis_up_to(1))

    def test_sumOfEvensUpTo2(self):
        self.assertEqual(2, sum_of_even_fibonaccis_up_to(2))

    def test_sumOfEvensUpTo8(self):
        self.assertEqual(10, sum_of_even_fibonaccis_up_to(8))

    def test_sumOfEvensUpTo33(self):
        self.assertEqual(10, sum_of_even_fibonaccis_up_to(33))

    def test_sumOfEvensUpTo34(self):
        self.assertEqual(44, sum_of_even_fibonaccis_up_to(34))

    def test_sumOfEvensUpTo143(self):
        self.assertEqual(44, sum_of_even_fibonaccis_up_to(143))

    def test_sumOfEvensUpTo144(self):
        self.assertEqual(188, sum_of_even_fibonaccis_up_to(144))

    def test_sumOfEvensUpTo4Million(self):
        self.assertEqual(4613732, sum_of_even_fibonaccis_up_to(4 * 1000 * 1000))


if __name__ == '__main__':
    unittest.main()
