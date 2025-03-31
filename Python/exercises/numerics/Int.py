def square_root(x):
    if x < 0:
        return None
    return x ** .5

def is_armstrong_number(number):
    total = 0
    num_string = str(number)
    digits = len(num_string)
    for num_char in num_string:
        total = total + (int(num_char)**digits)
    return total == number