#!/usr/bin/env python3

import sys

if len(sys.argv) != 1:
    print("none")
else:

    i = 0
    begin = 1
    lim = 10

    while i < (begin + lim):
        print(f"Table of {i}:", end=" ")        
        j = 0
        while j < (begin + lim):
            the_result = i * j
            print(the_result, end=" ")
            j += 1
        print()
        i += 1
