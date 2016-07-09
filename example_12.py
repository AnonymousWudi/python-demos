# coding=utf-8

if __name__ == '__main__':
    n, s, l = raw_input().split()
    n, s, l = int(n), int(s), int(l)
    songs = l / (s + 1) if l != s else l / s
    if songs % 13 == 0:
        result = n / (songs - 1) + 1 if n % (songs - 1) != 0 else n / (songs - 1)
    else:
        result = n / songs + 1 if n % songs != 0 else n / songs
    if result == 1 and n % 13 == 0:
        result += 1
    print result