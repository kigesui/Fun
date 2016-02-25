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


SKIP_CHARS = [' ']
SKIP_ENCODE_CHARS = ['\'', '/', ']', '?', '"', '}']


def encode_char(ch):
    if ch in SKIP_CHARS:
        return ch
    if ch in SKIP_ENCODE_CHARS:
        return ch
    for entry in MY_MAP:
        if ch == entry.m:
            return entry.e
    return 'FUCK'


def decode_char(ch):
    if ch in SKIP_CHARS:
        return ch
    for entry in MY_MAP:
        if ch == entry.e:
            return entry.m
    return 'FUCK'


def decode(cipher):
    return ''.join([decode_char(ch) for ch in cipher])


def encode(mesasge):
    return ''.join([encode_char(ch) for ch in mesasge])


# print decode('og upi vtsvl yjod. o esmy yp [;su eoyj upi/')




