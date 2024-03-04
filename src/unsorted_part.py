def find_unsorted_part(array):
    length = len(array) - 1
    left_unsorted_index = -1
    right_unsorted_index = -1
    for i in range(length):
        if array[i] > array[i + 1]:
            left_unsorted_index = i
            break
    if left_unsorted_index == -1:
        return -1, -1
    for i in range(length):
        if array[length - i] < array[length - i - 1]:
            right_unsorted_index = length - i + 1
            break
    if right_unsorted_index > length:
        right_unsorted_index = length
    min_unsorted = max_unsorted = array[left_unsorted_index]
    for i in range(left_unsorted_index, right_unsorted_index):
        if array[i] > max_unsorted:
            max_unsorted = array[i]
        if array[i] < min_unsorted:
            min_unsorted = array[i]
    for i in range(left_unsorted_index):
        if array[i] > min_unsorted:
            left_unsorted_index = i
            break
    for i in range(right_unsorted_index, length):
        if array[i] < max_unsorted:
            right_unsorted_index = i
            break
    return left_unsorted_index, right_unsorted_index
