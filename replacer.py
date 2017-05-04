#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

import argparse
import sys
from alphabet import LATIN_ALPHA
try:
    reduce
except NameError:
    from functools import reduce


def to_matrix(text):
    matrices = map(lambda x: LATIN_ALPHA[x], text)
    flatten = reduce(
        lambda acc, x: [acc_ + x_ for (acc_, x_) in zip(acc, x)], 
        matrices,
    )
    return flatten


def to_emoji(matrix, bg, fg):
    emojies = [
        map(lambda x: fg if x else bg, row)
        for row in matrix
    ]
    return '\n'.join([''.join(es) for es in emojies])


def transform(text, bg, fg):
    return to_emoji(to_matrix(text.upper()), bg=bg, fg=fg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Write text with emojis')
    parser.add_argument('text', type=str,
                        help='quoted text to write into emoji')
    parser.add_argument('--fg', type=str, dest='fg', default='■',
                        help='character or quoted text to use as foreground')
    parser.add_argument('--bg', type=str, dest='bg', default='□',
                        help='character or quoted text to use as background')
    args = parser.parse_args()
    print(transform(args.text, bg=args.bg, fg=args.fg))
