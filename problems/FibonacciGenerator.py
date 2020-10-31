class FibonacciGenerator(object):
    """ FibonacciGenerator implements either an iterator for fibonacci numbers up to a given limit or a generator of fibonacci numbers

        usage as iterator:
        list(FibonacciGenerator(33)) == [0, 1, 1, 2, 3, 5, 8, 13, 21]
        list(FibonacciGenerator(34)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        list(FibonacciGenerator(35)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

        usage as generator:
        fg = FibonacciGenerator()
        fg.next() as many times as you want

        but list(FibonacciGenerator()) raises an OverflowError

    """
    def __init__(self, limit=-1):
        self.previous = -2
        self.current = -1
        self.limit = limit

    def __iter__(self):
        if self.limit < 0:
            raise OverflowError
        return self

    def __next__(self):
        if self.previous < 0:
            self.previous += 1
            self.current += 1
        else:
            result = self.previous + self.current
            if -1 < self.limit < result:
                raise StopIteration
            self.previous = self.current
            self.current = result

        return self.current

    def next(self):
        return self.__next__()