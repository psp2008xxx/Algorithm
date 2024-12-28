from ..quick_sort import quick_sort


def test_quick_sort():
    arr = [3, 4, 2, 9, 0, 2]
    result = quick_sort(arr)
    assert result == [0, 2, 2, 3, 4, 9]