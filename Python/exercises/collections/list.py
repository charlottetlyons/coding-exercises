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

def length_of_max_value(some_list):
    return len(str(max(some_list)))

def bubble_sort(some_list):
    for i in range(len(some_list) - 1):
        for j in range(i + 1, len(some_list)):
            if some_list[i] > some_list[j]:
                some_list[i], some_list[j] = some_list[j], some_list[i]
    return some_list

def selection_sort(some_list):
    for i in range(len(some_list) - 1):
        min_index = i
        for j in range(i + 1, len(some_list)):
            if some_list[j] < some_list[min_index]:
                min_index = j
        if min_index != i:
            some_list[i], some_list[min_index] = some_list[min_index], some_list[i]
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

def quick_sort(some_list):
    return quick_sort_helper(some_list, 0, len(some_list) - 1)


def quick_sort_helper(some_list, left, right):
    if left <= right:
        pivot_index = pivot(some_list, left, right)
        quick_sort_helper(some_list, left, pivot_index - 1)
        quick_sort_helper(some_list, pivot_index + 1, right)
    return some_list

def pivot(some_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if some_list[i] < some_list[pivot_index]:
            swap_index += 1
            swap(some_list, swap_index, i)
    swap(some_list, pivot_index, swap_index)
    return swap_index

def swap(some_list, a, b):
    some_list[a], some_list[b] = some_list[b], some_list[a]
