# Array = [5,6,7,8]


# Selection Sort find the smallest in an array and return indice
# remove from the orginal array
# append to new array value

test_list = [3, 6, 8, 2, 9, 1, 20]


def smallest(arr):
    smallest = None
    new_index = None
    for index, num in enumerate(arr):
        if smallest is None:
            smallest = num
            new_index = index
        elif num < smallest:
            smallest = num
            new_index = index
    return new_index


def recurse_select_sort(arr, new_list=[]):
    if len(arr) > 0:
        new_list.append(arr.pop(smallest(arr)))
        return recurse_select_sort(arr, new_list)
    else:
        return new_list


print(smallest(test_list))

print(recurse_select_sort(test_list))
