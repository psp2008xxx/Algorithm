from ..recursive_function import count_down, factorial


def test_count_down(capsys):
    count_down(3)
    captured = capsys.readouterr()
    expected = "3\n2\n1\n"
    assert captured.out == expected


def test_factorial():
    result = factorial(3)
    assert result == 6
