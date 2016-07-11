# coding=utf-8


def getDrinkNum(bottles):
    if bottles in (0, 1):
        return 0
    elif bottles in (2, 3):
        return 1
    else:
        return bottles / 3 + getDrinkNum(bottles / 3 + bottles % 3)


if __name__ == '__main__':
    while True:
        bottles = int(raw_input())
        if not bottles:
            break

        print getDrinkNum(bottles)