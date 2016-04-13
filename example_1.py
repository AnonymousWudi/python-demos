# coding=utf-8

from PIL import Image
import argparse

# input parameters
parser = argparse.ArgumentParser()

parser.add_argument('file')     # input file
parser.add_argument('-o', '--output')   # output file
parser.add_argument('--width', type=int, default=80)   # output file width
parser.add_argument('--height', type=int, default=40)  # output file height

# get all the input parameters
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 256 kind of gray level --> 70 chars
def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    print IMG
    im = Image.open("./images/%s" % IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print txt

    # draw output file
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("./outputs/example_1.txt", 'w') as f:
            f.write(txt)
