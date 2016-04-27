#!/usr/bin/env python

import argparse
from collections import namedtuple


class FunException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


MapEntry = namedtuple('MapEntry', ['m', 'e'])

MY_MAP = []

KEYBOARD = [
    ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='       ],
    [      'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
    [       'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\''         ],
    [        'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'              ],

    ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+'       ],
    [      'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|' ],
    [       'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"'          ],
    [        'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?'              ]
]

for row in KEYBOARD:
    row_len = len(row)
    for i in xrange(row_len):
        orig_index = i
        enco_index = (i+1) % row_len
        MY_MAP.append(MapEntry(m=row[orig_index], e=row[enco_index]))

SKIP_CHARS = [' ']
SKIP_ENCODE_CHARS = []  # ['\'', '/', ']', '?', '"', '}']

SKIP_DECODE_SEQUENCE = []  # [', ', '. ']


def encode_char(ch):
    if ch in SKIP_CHARS:
        return ch
    if ch in SKIP_ENCODE_CHARS:
        return ch
    for entry in MY_MAP:
        if ch == entry.m:
            return entry.e
    return 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'


def decode_char(ch):
    if ch in SKIP_CHARS:
        return ch
    for entry in MY_MAP:
        if ch == entry.e:
            return entry.m
    raise FunException("Unable to decode.")


def decode(encoded):
    lst = []
    for i in xrange(len(encoded)):
        ch = encoded[i]
        if ''.join(encoded[i:i+2]) in SKIP_DECODE_SEQUENCE:
            lst.append(ch)
        else:
            lst.append(decode_char(ch))
    return ''.join(lst)


def encode(plain):
    return ''.join([encode_char(ch) for ch in plain])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--encode", type=str, nargs='+', metavar='STR',
                        help="Encode the given string STR.")
    parser.add_argument("-d", "--decode", type=str, nargs='+', metavar='STR',
                        help="Decode the given string STR.")

    args = parser.parse_args()

    if not (args.encode or args.decode):
        parser.print_usage()
        return

    if args.encode:
        for orig in args.encode:
            print("--------------")
            print("Original:" + orig)
            print("Encoded :" + encode(orig))

    if args.decode:
        for orig in args.decode:
            print("--------------")
            print("Original:" + orig)
            print("Decoded :" + decode(orig))


if __name__ == '__main__':
    main()
