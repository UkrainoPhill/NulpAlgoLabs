def find_unsorted_part(arr):
    length = len(arr) - 1
    left = -1
    right = -1
    for i in range(length):
        if arr[i] > arr[i + 1]:
            left = i
            break
    if left == -1:
        return -1, -1
    for i in range(length):
        if arr[length - i] < arr[length - i - 1]:
            right = length - i + 1
            break
    if right > length:
        right = length
    min_unsorted = max_unsorted = arr[left]
    for i in range(left, right):
        if arr[i] > max_unsorted:
            max_unsorted = arr[i]
        if arr[i] < min_unsorted:
            min_unsorted = arr[i]
    for i in range(left):
        if arr[i] > min_unsorted:
            left = i
            break
    for i in range(right, length):
        if arr[i] < max_unsorted:
            right = i
            break
    return left, right
