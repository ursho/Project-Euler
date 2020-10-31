class Problem0002(object):
    previous = -2
    current = -1

    def next_fibonacci(self):
        if self.previous < 0:
            self.previous += 1
            self.current += 1
        else:
            result = self.previous + self.current
            self.previous = self.current
            self.current = result

        return self.current


def sum_of_evens_up_to(inclusive_limit):
    result = 0
    problem = Problem0002()
    f = problem.next_fibonacci()
    while f <= inclusive_limit:
        if (f % 2) == 0:
            result = result + f
        print(f, result)
        f = problem.next_fibonacci()
    return result
