#!/usr/bin/env python3

import sys
import re
from textwrap import dedent


header = dedent('''\
    #define GEN_SET_INCLUDE_LEVEL(hash, level) hash ## define SET_INCLUDE INCLUDE_LEVEL level
    ''')

pat = re.compile(r'^\s*#\s+' # e.g. '# '
                 r'(?P<lineno>\d+)\s+' # e.g. '25 '
                 r'"(?P<file>.*)"' # e.g. '"<stdin>"'
                 r'(?P<flags>(\s+\d+)*\s*)$') # e.g. '1 3 4'


def main():
    starting = True
    stack = []

    for i, l in enumerate(sys.stdin.readlines()):
        try:
            match = pat.match(l)
            if match:
                flags = list(map(int, match.group('flags').split()))
                file = match.group('file')
                if starting or 1 in flags:
                    assert 2 not in flags
                    stack.append(file)
                    print('  '*(len(stack)-1), file, sep='', file=sys.stderr)
                    if starting:
                        assert 1 not in flags
                        starting = False
                    else: # 1 in flags
                        print(f'#if !defined(SWIG_INCLUDE_LEVEL) || '
                              f'SWIG_INCLUDE_LEVEL >= {len(stack)-1}')
                elif 2 in flags:
                    stack.pop()
                    assert file == stack[-1]
                    print('#endif')
            print(l)
        except:
            print(f'error in line {i}:\n{l}', file=sys.stderr)
            raise


if __name__ == '__main__':
    main()
