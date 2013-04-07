#!/usr/bin/env python

from PIL import Image
import sys

ks = ['&', '$', 'S', '7', 'I', ';', ':', ',', '.', ' ']
level = len(ks)

def img_data(img):
    """ convert image object to martrix data. """
    return [list(img.crop((0, y, img.size[0], y+1)).getdata()) for y in range(0, img.size[1])]

def row2str(row):
    """ convert an array to ascii string """
    return "".join([ ks[i-1] for i in row ])

def img2ascii(img_path, dx=1, dy=1):
    """ input : image path and ratio
        output: ascii art """
    img = Image.open(img_path).convert("L")
    new_size = ( int(img.size[0]*dx), int(img.size[1]*dy) )
    img = img.resize(new_size)
    data = img_data(img)

    max_color = max([max(row) for row in data])
    min_color = min([min(row) for row in data])
    depth = max_color - min_color
    div = depth/level
    if depth == 0: div = 1      # this is an error case

    processed = map(lambda lx: [ i - min_color for i in lx ], data)
    return [ row2str(map(lambda x: x/div, row)) for row in processed ]

def main():
    """ cli """
    dx, dy = 1, 1
    f = sys.argv[1]
    args = sys.argv[2:]
    if len(args) == 1: dx = float(args[0])
    if len(args) == 2: dx, dy = float(args[0]), float(args[1])

    ascii = img2ascii(f, dx, dy)
    for i in ascii: print i

if __name__ == "__main__":
    main()
