# coding=utf-8


def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 0
    if a > b:
        b, a = a, b
    if b > c:
        c, b = b, c
    if a > b:
        b, a = a, b
    if c * c > a * a + b * b:
        return 3
    elif c * c == a * a + b * b:
        return 2
    else:
        return 1


if __name__ == '__main__':
    print triangle_type(4, 5, 3)
