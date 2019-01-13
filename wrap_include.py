#!/usr/bin/env python3

import re
import sys
from textwrap import dedent


header = dedent('''\
    #define PRE_INCLUDE_1 #ifdef SWIG
    #define PRE_INCLUDE_2 #else
    #define POST_INCLUDE #endif
    ''')

pat = re.compile(r'^[^\S\n]*#\s*include.*$', flags=re.MULTILINE)

repl = dedent('''\
    PRE_INCLUDE_1
    PRE_INCLUDE_2
    \\g<0>
    POST_INCLUDE
    ''')


def main():
    print(header, end='')

    src = sys.stdin.read()
    print(pat.sub(repl, src), end='')


if __name__ == '__main__':
    main()
