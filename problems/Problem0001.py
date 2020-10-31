def sum(divisor1, divisor2, limit):
    s = 0
    for x in range(limit):
        if x % divisor1 == 0 or x % divisor2 == 0:
            s = s + x
    return s
