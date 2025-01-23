def square_root(x):
    if x < 0:
        return None
    return x**0.5

def is_armstrong_number(number):
    total = 0
    number_string = str(number)
    number_len = len(number_string)
    for char in number_string:
        digit = int(char)
        total = total + digit ** number_len
    return total == number
