def square_root(x):
    if x < 0:
        return None
    return x ** .5

def is_armstrong_number(number):
    total = 0
    num_string = str(number)
    for digit_char in num_string:
        digit = int(digit_char)
        total = total + digit ** len(num_string)
    return total == number
