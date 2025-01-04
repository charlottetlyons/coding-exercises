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
        for j in range(i+1, len(some_list)):
            if some_list[i] > some_list[j]:
                some_list[i], some_list[j] = some_list[j], some_list[i]
    return some_list

def selection_sort(some_list):
    for i in range(len(some_list) - 1):
        min_index = i
        for j in range(i+1, len(some_list)):
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