#!/usr/bin/env python2
import sys
from alphabet import LATIN_ALPHA


def to_matrix(text):
    matrices = map(lambda x: LATIN_ALPHA[x], text)
    flatten = reduce(
        lambda acc, x: [acc_ + x_ for (acc_, x_) in zip(acc, x)], 
        matrices,
    )
    return flatten


def to_emoji(matrix, bg=':awesome:', fg=':narkoman:'):
    emojies = [
        map(lambda x: fg if x else bg, row)
        for row in matrix
    ]
    return '\n'.join([''.join(es) for es in emojies])


def transform(text, bg=':awesome:', fg=':narkoman:'):
    return to_emoji(to_matrix(text.upper()), bg=bg, fg=fg)


if __name__ == '__main__':
    word = sys.argv[1]
    bg = ':awesome:'
    fg = ':narkoman:'
    if len(sys.argv) == 4:
        bg = sys.argv[2]
        fg = sys.argv[3]
    print(transform(word, bg=bg, fg=fg))
