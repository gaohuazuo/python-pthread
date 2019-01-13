#!/usr/bin/env python3

import re
from subprocess import check_output, DEVNULL


ident = rf'[_a-zA-Z][_a-zA-Z0-9]*' # e.g. __cplusplus
arg_list = rf'\({ident}(:?,\s*{ident})*\)' # e.g. (a, b, c)
pat = re.compile(rf'^#define ({ident})(:?{arg_list})? .*$')

def repl(match):
    return [
        '#ifdef %s' % match.group(1),
        '#else',
        match.group(0),
        '#endif'
    ]


def main():
    defs = check_output(['clang', '-std=c11', '-dM', '-E', '-'],
                        stdin=DEVNULL, universal_newlines=True)

    for l in defs.splitlines():
        if l:
            for o in repl(pat.match(l)):
                print(o)


if __name__ == '__main__':
    main()
