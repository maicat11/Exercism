def binary_search(list_of_numbers, number):

    if not list_of_numbers:
        raise ValueError('Empty list')

    min_val = 0
    max_val = len(list_of_numbers) - 1

    while max_val >= min_val:
        mid_pt = (min_val + max_val) // 2
        if list_of_numbers[mid_pt] == number:
            return mid_pt
        if list_of_numbers[mid_pt] > number:
            max_val = mid_pt - 1
        else:
            min_val = mid_pt + 1
    raise ValueError('Number not found.')
