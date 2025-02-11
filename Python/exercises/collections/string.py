def first_unique_character(string):
    count = {}

    for char in string:
        count[char] = count.get(char, 0) + 1

    for char in string:
        if count[char] == 1:
            return char
    return None

def is_anagrams(string_a, string_b):
    cleaned_a = string_a.replace(" ", "").lower()
    cleaned_b = string_b.replace(" ", "").lower()

    if len(cleaned_a) != len(cleaned_b):
        return False

    char_count = {}

    for char in cleaned_a:
        char_count[char] = char_count.get(char, 0) + 1

    for char in cleaned_b:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    return True