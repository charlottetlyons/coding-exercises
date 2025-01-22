def square_root(x):
    if x < 0:
        return None
    return x**0.5

def is_armstrong_number(number):
    total = 0
    numberString = str(number)
    len_of_digit = len(numberString)
    for digitString in numberString:
        digit = int(digitString)
        raised_digit = digit**len_of_digit
        total = total + raised_digit
    return total == number
