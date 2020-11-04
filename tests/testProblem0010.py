import unittest
from math import isqrt
from concurrent.futures import ThreadPoolExecutor


def is_prime(n):
    if n < 2:
        return 0
    if n == 2:
        return n
    if n % 2 == 0:
        return 0

    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0:
            return 0
    return n

def prime_candidates(limit):
    yield 2
    yield 3
    n = 6
    while n <= limit:
        yield n - 1
        if n + 1 < limit:
            yield n + 1
        n += 6

class TestProblem0010(unittest.TestCase):
    def test_primes_up_to_10(self):
        with ThreadPoolExecutor() as executor:
            self.assertEqual(17, sum(executor.map(is_prime, prime_candidates(10))))

    def test_primes_up_to_2000000(self):
        with ThreadPoolExecutor() as executor:
            self.assertEqual(142913828922, sum(executor.map(is_prime, prime_candidates(2 * 1000 * 1000))))


if __name__ == '__main__':
    unittest.main()
