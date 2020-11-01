def is_palindrome(number):
    digits = [x for x in str(number)]
    if len(digits) % 2 != 0:
        return False
    for i in range(len(digits) // 2):
        if digits[i] != digits[-i - 1]:
            return False
    return True


def find_greatest_palindrome():
    largest_palindrome = 0
    a = 999
    while a >= 100:
        b = a
        while b >= 100:
            c = a * b
            if is_palindrome(c):
                largest_palindrome = max(largest_palindrome, c)
            b -= 1
        a -= 1
    return largest_palindrome
