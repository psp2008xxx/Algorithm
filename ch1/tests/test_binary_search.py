from ..binary_search import binary_search

arr = [1, 3, 5, 7, 9]


def test_exist_item():
    index = binary_search(arr, 3)
    assert index == 1

def test_no_exist_item():
    index = binary_search(arr, -1)
    assert index is None


