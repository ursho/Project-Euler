from problems.Primes import prime_factors_of


def palindrome_of_3(half):
    return ((half * 10 + half % 10) * 10 + half // 10 % 10) * 10 + half // 100


def build_3_digit_factor(factors, first_factor):
    while len(factors) > 0 and first_factor * factors[0] < 1000:
        first_factor *= factors[0]
        factors = factors[1:len(factors)]
    return factors, first_factor


def find_greatest_palindrome():
    half = 999
    while half > 99:
        palindrome = palindrome_of_3(half)
        factors = prime_factors_of(palindrome)
        if factors[-1] < 1000:
            factors, first_factor = build_3_digit_factor(factors, factors.pop())
            factors, second_factor = build_3_digit_factor(factors, 1)

            print(palindrome, prime_factors_of(palindrome), [first_factor, second_factor], factors)

            if len(factors) == 0:
                return palindrome
        half -= 1
    raise ValueError
