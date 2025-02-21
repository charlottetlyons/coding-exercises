def square_root(x):
    if x < 0:
        return None
    return x ** .5

def is_armstrong_number(number):
    total = 0
    number_string = str(number)
    length_of_number = len(number_string)
    for digit_string in number_string:
        digit = int(digit_string)
        total = total + (digit ** length_of_number)
    return total == number
