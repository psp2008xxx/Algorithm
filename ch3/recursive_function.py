def count_down(num):
    print(num)
    if num <= 1:
        return
    else:
        count_down(num - 1)


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
