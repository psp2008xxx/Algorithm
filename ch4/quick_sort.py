def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])


def recursive_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], recursive_max(arr[1:]))


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def multiplication(arr):
    result = []
    for i in arr:
        result.append([i * j for j in arr])
    return result
