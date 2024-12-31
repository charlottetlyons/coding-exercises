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