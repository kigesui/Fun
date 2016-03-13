#!/usr/bin/env python

import argparse
from collections import namedtuple

MapEntry = namedtuple('MapEntry', ['m', 'e'])

MY_MAP = []

MY_MAP.append(MapEntry('1', e='2'))
MY_MAP.append(MapEntry('2', e='3'))
MY_MAP.append(MapEntry('3', e='4'))
MY_MAP.append(MapEntry('4', e='5'))
MY_MAP.append(MapEntry('5', e='6'))
MY_MAP.append(MapEntry('6', e='7'))
MY_MAP.append(MapEntry('7', e='8'))
MY_MAP.append(MapEntry('8', e='9'))
MY_MAP.append(MapEntry('9', e='0'))
MY_MAP.append(MapEntry('0', e='-'))
MY_MAP.append(MapEntry('-', e='='))

MY_MAP.append(MapEntry('q', e='w'))
MY_MAP.append(MapEntry('w', e='e'))
MY_MAP.append(MapEntry('e', e='r'))
MY_MAP.append(MapEntry('r', e='t'))
MY_MAP.append(MapEntry('t', e='y'))
MY_MAP.append(MapEntry('y', e='u'))
MY_MAP.append(MapEntry('u', e='i'))
MY_MAP.append(MapEntry('i', e='o'))
MY_MAP.append(MapEntry('o', e='p'))
MY_MAP.append(MapEntry('p', e='['))
MY_MAP.append(MapEntry('[', e=']'))

MY_MAP.append(MapEntry('a', e='s'))
MY_MAP.append(MapEntry('s', e='d'))
MY_MAP.append(MapEntry('d', e='f'))
MY_MAP.append(MapEntry('f', e='g'))
MY_MAP.append(MapEntry('g', e='h'))
MY_MAP.append(MapEntry('h', e='j'))
MY_MAP.append(MapEntry('j', e='k'))
MY_MAP.append(MapEntry('k', e='l'))
MY_MAP.append(MapEntry('l', e=';'))
MY_MAP.append(MapEntry(';', e='\''))

MY_MAP.append(MapEntry('z', e='x'))
MY_MAP.append(MapEntry('x', e='c'))
MY_MAP.append(MapEntry('c', e='v'))
MY_MAP.append(MapEntry('v', e='b'))
MY_MAP.append(MapEntry('b', e='n'))
MY_MAP.append(MapEntry('n', e='m'))
MY_MAP.append(MapEntry('m', e=','))
MY_MAP.append(MapEntry(',', e='.'))
MY_MAP.append(MapEntry('.', e='/'))

MY_MAP.append(MapEntry('!', e='@'))
MY_MAP.append(MapEntry('@', e='#'))
MY_MAP.append(MapEntry('#', e='$'))
MY_MAP.append(MapEntry('$', e='%'))
MY_MAP.append(MapEntry('%', e='^'))
MY_MAP.append(MapEntry('^', e='&'))
MY_MAP.append(MapEntry('&', e='*'))
MY_MAP.append(MapEntry('*', e='('))
MY_MAP.append(MapEntry('(', e=')'))
MY_MAP.append(MapEntry(')', e='_'))
MY_MAP.append(MapEntry('_', e='+'))

MY_MAP.append(MapEntry('Q', e='W'))
MY_MAP.append(MapEntry('W', e='E'))
MY_MAP.append(MapEntry('E', e='R'))
MY_MAP.append(MapEntry('R', e='T'))
MY_MAP.append(MapEntry('T', e='Y'))
MY_MAP.append(MapEntry('Y', e='U'))
MY_MAP.append(MapEntry('U', e='I'))
MY_MAP.append(MapEntry('I', e='O'))
MY_MAP.append(MapEntry('O', e='P'))
MY_MAP.append(MapEntry('P', e='{'))
MY_MAP.append(MapEntry('{', e='}'))

MY_MAP.append(MapEntry('A', e='S'))
MY_MAP.append(MapEntry('S', e='D'))
MY_MAP.append(MapEntry('D', e='F'))
MY_MAP.append(MapEntry('F', e='G'))
MY_MAP.append(MapEntry('G', e='H'))
MY_MAP.append(MapEntry('H', e='J'))
MY_MAP.append(MapEntry('J', e='K'))
MY_MAP.append(MapEntry('K', e='L'))
MY_MAP.append(MapEntry('L', e=':'))
MY_MAP.append(MapEntry(':', e='\"'))

MY_MAP.append(MapEntry('Z', e='X'))
MY_MAP.append(MapEntry('X', e='C'))
MY_MAP.append(MapEntry('C', e='V'))
MY_MAP.append(MapEntry('V', e='B'))
MY_MAP.append(MapEntry('B', e='N'))
MY_MAP.append(MapEntry('N', e='M'))
MY_MAP.append(MapEntry('M', e='<'))
MY_MAP.append(MapEntry('<', e='>'))
MY_MAP.append(MapEntry('>', e='?'))


SKIP_CHARS = [' ']
SKIP_ENCODE_CHARS = ['\'', '/', ']', '?', '"', '}']

SKIP_DECODE_SEQUENCE = [', ', '. ']


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
    return 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'


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
