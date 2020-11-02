from math import isqrt


def prime_factors_of(number):
    """ returns the list of prime factors of the given number
    >>> prime_factors_of(24)
    [2, 2, 2, 3]
    """
    limit = isqrt(number)

    factors = []
    remaining_number = number
    while remaining_number > 1:

        factor = 2
        factor_candidate = remaining_number

        while factor <= limit:
            if remaining_number % factor == 0:
                factor_candidate = factor
                break
            else:
                factor = factor + 1

        factors = factors + [factor_candidate]
        remaining_number = remaining_number // factor_candidate

    return factors


def least_common_multiple_of_numbers_up_to(limit):
    numbers = list(range(2, limit + 1))
    for j in range(len(numbers) - 1):
        for i in range(j + 1, len(numbers)):
            if numbers[i] % numbers[j] == 0:
                numbers[i] //= numbers[j]
    result = 1
    for f in numbers:
        result *= f

    return result


def least_common_multiple_of(*numbers):
    class Counter(dict):
        def __missing__(self, key):
            return 0

    total_factors_count = Counter()
    for n in numbers:
        factors_count = Counter()
        for factor in prime_factors_of(n):
            factors_count[factor] += 1
        for factor in iter(factors_count):
            total_factors_count[factor] = max(total_factors_count[factor], factors_count[factor])

    result = 1
    for factor in iter(total_factors_count):
        result *= pow(factor, total_factors_count[factor])

    return result


def nth_prime(number):
    primes = [2, 3]

    def is_prime(n):
        for p in primes:
            if n % p == 0:
                return False
        return True

    # All primes greater than 3 can be written in the form 6k+/-1
    def candidate_generator():
        n = 6
        while True:
            yield n - 1
            yield n + 1
            n += 6

    generator = candidate_generator()
    while len(primes) < number:
        candidate = next(generator)
        if is_prime(candidate):
            primes += [candidate]

    if number == 1:
        return primes[0]

    return primes[-1]
