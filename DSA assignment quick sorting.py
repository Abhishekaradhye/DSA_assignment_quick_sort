'Quick sort the test array '

def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]  # Choose the pivot element
    left = [x for x in array if x < pivot]  # Elements less than the pivot
    middle = [x for x in array if x == pivot]  # Elements equal to the pivot
    right = [x for x in array if x > pivot]  # Elements greater than the pivot

    # Recursively sort the left and right sublists, then concatenate them with the middle list
    return quicksort(left) + middle + quicksort(right)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))


