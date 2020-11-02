import unittest

#   (a + b + c)^2 - a^2 -b^2 - c^2
# = a^2 + 2ab + 2ac + b^2 + 2bc + c^2 - a^2 -b^2 - c^2
# = 2ab + 2ac + 2bc
def sum_of_square_difference(limit):
    s = 0
    for i in range(1, limit +1):
        for j in range(i+1, limit+1):
            s += 2 * i * j
    return s


class TestProblem0006(unittest.TestCase):
    def test_sum_square_difference(self):
        self.assertEqual(2640, sum_of_square_difference(10))
        self.assertEqual(25164150, sum_of_square_difference(100))



if __name__ == '__main__':
    unittest.main()
