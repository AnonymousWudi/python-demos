# coding=utf-8

import itertools


def power(s):
    result = []
    for i in range(0, len(s) + 1):
        result.extend(list(list(x) for x in itertools.combinations(s, i)))
    return result

if __name__ == '__main__':
    print power([1, 2, 3])
