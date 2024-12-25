def find_smallest(arr):
    smallest_item = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_item:
            smallest_item = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    copy_list = list(arr)
    for i in range(len(copy_list)):
        smallest_index = find_smallest(copy_list)
        new_arr.append(copy_list.pop(smallest_index))
    return new_arr