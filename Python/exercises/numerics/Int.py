def square_root(x):
    if x < 0:
        return None
    return x ** .5

def is_armstrong_number(number):
    total = 0
    number_string = str(number)
    number_of_digits = len(number_string)
    for digit_char in number_string:
        digit = int(digit_char)
        total = total + (digit ** number_of_digits)
    return total == number

def swap_without_third(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_odd_even(n):
    if not isinstance(n, int) or isinstance(n, bool):
        return "non-integer"

    if n & 1:
        return "odd"
    else:
        return "even"

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n ** .5) + 1
    for factor in range(3, limit, 2):
        if n % factor == 0:
            return False
    return True