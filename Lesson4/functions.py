""""""
def my_range(a, b, c=1):
    x = a
    while a <= x < b:
        yield x
        x += c
