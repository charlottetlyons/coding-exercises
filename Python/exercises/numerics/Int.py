def square_root(n):
    if n < 0:
        return None
    return n ** .5

def is_armstrong_number(number):
    total = 0
    number_string = str(number)
    number_of_digits = len(number_string)
    for digit_char in number_string:
        digit = int(digit_char)
        total += (digit ** number_of_digits)
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
    if not isinstance(n, int):
        return "non-integer"

    if n & 1:
        return "odd"
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

def is_palindrome(n):
    num_string = str(n)
    for i in range(len(num_string) // 2):
        if num_string[i] != num_string[len(num_string) - i - 1]:
            return False
    return True

def prime_factors(n):
    if n is None or n < 2:
        return None

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for factor in range(3, int(n ** .5) + 1, 2):
        while n % factor == 0:
            factors.append(factor)
            n = n // factor
    if n > 2:
        factors.append(n)
    return factors

def get_digit(num, digit_pos):
    return abs(num) // (10 ** digit_pos) % 10
