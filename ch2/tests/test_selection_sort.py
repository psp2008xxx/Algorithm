from ..selection_sort import selection_sort


def test_selection_sort():
    input_array = [5, 3, 6, 2, 10]
    output_array = selection_sort(input_array)
    assert output_array == [2, 3, 5, 6, 10]