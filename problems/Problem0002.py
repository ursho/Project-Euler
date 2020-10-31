from problems.FibonacciGenerator import FibonacciGenerator

def sum_of_even_fibonaccis_up_to(inclusive_limit):
    fibonacci_numbers = list(FibonacciGenerator(inclusive_limit))
    even_fibonacci_numbers = filter(lambda f: f % 2 == 0, fibonacci_numbers)
    return sum(even_fibonacci_numbers)
