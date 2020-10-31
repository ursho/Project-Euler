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

        lowest_possible_factor = 2
        factor_candidate = remaining_number

        while lowest_possible_factor <= limit:
            if remaining_number % lowest_possible_factor == 0:
                factor_candidate = lowest_possible_factor
                break
            else:
                lowest_possible_factor = lowest_possible_factor + 1

        factors = factors + [factor_candidate]
        remaining_number = remaining_number // factor_candidate

    return factors
