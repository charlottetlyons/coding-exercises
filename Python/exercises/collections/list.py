from random import randint

# LIST FUNCTIONS
def access_indices(some_list):
    indices = []
    for i in range(len(some_list)):
        indices.append(i)
    return indices

def max_value(some_list):
    max_value = 0
    for i in some_list:
        if i > max_value:
            max_value = i
    return max_value

def min_max_tuple(some_list):
    if len(some_list) == 0:
        return None

    min, max = some_list[0], some_list[0]
    for num in some_list:
        if num < min:
            min = num
        if num > max:
            max = num
    return (min, max)

def length_of_max_value(some_list):
    return len(str(max(some_list)))

def bubble_sort(some_list):
    for i in range(len(some_list) - 1):
        for j in range(i + 1, len(some_list)):
            if some_list[i] > some_list[j]:
                some_list[i], some_list[j] = some_list[j], some_list[i]
    return some_list

def selection_sort(some_list):
    if len(some_list) <= 1:
        return some_list
    
    for i in range(len(some_list) - 1):
        min_index = i
        for j in range(i+1, len(some_list)):
            if some_list[j] < some_list[min_index]:
                min_index = j
        if min_index is not i:
            swap(some_list, min_index, i)
    return some_list

def insertion_sort(some_list):
    for i in range(1, len(some_list)):
        current_value = some_list[i]
        position = i - 1
        while current_value < some_list[position] and position > -1:
            some_list[position + 1] = some_list[position]
            some_list[position] = current_value
            position -= 1
    return some_list

def merge_sort(some_list):
    if len(some_list) <= 1:
        return some_list

    mid_index = len(some_list) // 2
    left = merge_sort(some_list[:mid_index])
    right = merge_sort(some_list[mid_index:])

    return merge(left, right)

def merge(list1, list2):
    combined = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

def quick_sort(some_list):
    def pivot(some_list, pivot_index, end_index):
        swap_index = pivot_index
        for i in range(pivot_index + 1, end_index + 1):
            if some_list[i] < some_list[pivot_index]:
                swap_index += 1
                swap(some_list, swap_index, i)
        swap(some_list, pivot_index, swap_index)
        return swap_index


    def quick_sort_helper(some_list, left, right):
        if left <= right:
            pivot_index = pivot(some_list, left, right)
            quick_sort_helper(some_list, left, pivot_index - 1)
            quick_sort_helper(some_list, pivot_index + 1, right)
        return some_list
    return quick_sort_helper(some_list, 0, len(some_list) - 1)

# TODO: Test
def partition(some_list, left, right, pivot_value):
    while left <= right:
        while some_list[left] < pivot_value:
            left += 1
        while some_list[right] > pivot_value:
            right -= 1
        if left <= right:
            some_list[left], some_list[right] = some_list[right], some_list[left]
            left += 1
            right -= 1
    return left

# TODO: Test
def median_of_three(some_list, left, right):
    mid = (left + right) // 2
    a, b, c = some_list[left], some_list[mid], some_list[right]

    if a > b:
        if a < c:
            pivot_value = a
        elif b > c:
            pivot_value = b
        else:
            pivot_value = c
    else:
        if a > c:
            pivot_value = a
        elif b < c:
            pivot_value = b
        else:
            pivot_value = c
    return pivot_value

def median_of_three_quick_sort(some_list):
    def quick_sort_helper(some_list, left, right):
        if left < right:
            pivot_value = median_of_three(some_list, left, right)
            pivot_index = partition(some_list, left, right, pivot_value)
            quick_sort_helper(some_list, left, pivot_index - 1)
            quick_sort_helper(some_list, pivot_index, right)
        return some_list
    return quick_sort_helper(some_list, 0, len(some_list) - 1)

# TODO: Test
def randomized_pivot(some_list, left, right):
    random_index = randint(left, right)
    some_list[left], some_list[random_index] = some_list[random_index], some_list[left]
    return some_list[left]

def randomized_pivot_quick_sort(some_list):
    def quick_sort_helper(some_list, left, right):
        if left < right:
            pivot_value = randomized_pivot(some_list, left, right)
            pivot_index = partition(some_list, left, right, pivot_value)
            quick_sort_helper(some_list, left, pivot_index - 1)
            quick_sort_helper(some_list, pivot_index, right)
        return some_list
    return quick_sort_helper(some_list, 0, len(some_list) - 1)

def swap(some_list, a, b):
    some_list[a], some_list[b] = some_list[b], some_list[a]

def radix_sort(some_list):
    return

def get_digit(num, digit_pos):
    return (abs(num) // (10 ** digit_pos)) % 10

def pairs_equal_to_n(some_list, n):
    if len(some_list) <= 1:
        return []

    seen = set()
    pairs = set()

    for element in some_list:
        pair_value = n - element
        if pair_value in seen:
            pairs.add((min(element, pair_value), max(element, pair_value)))
        seen.add(element)
    return list(pairs)

def missing_of_n(int_list, n):
    expected = n * (n + 1) // 2
    total = 0
    for num in int_list:
        total += num
    return expected - total

def find_duplicates(some_list):
	seen = set() 
	duplicates = set() 
	for element in some_list: 
		if element in seen: 
			duplicates.add(element) 
		seen.add(element)
	return list(duplicates)

def remove_duplicates(some_list):
    seen = set()
    result = []
    for element in some_list:
        if element not in seen:
            result.append(element)
            seen.add(element)
    return result

def remove_occurrences(some_list, x):
    index = 0
    while index < len(some_list):
        if some_list[index] == x:
            some_list.pop(index)
        else:
            index += 1
    return len(some_list)

def shares_value(list1, list2):
    values = {}
    for i in list1:
        values[i] = True
    for j in list2:
        if j in values:
            return True
    return False

def longest_of_strings(strings):
    if len(strings) == 0:
        return None
    
    longest_string = ""

    for string in strings:
        string_length = len(string)
        if string_length  > len(longest_string):
            longest_string = string
    return longest_string
