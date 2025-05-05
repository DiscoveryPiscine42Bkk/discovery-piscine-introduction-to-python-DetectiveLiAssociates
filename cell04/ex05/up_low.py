#!/usr/bin/env python3

the_given_input = str(input().strip())

for i in the_given_input:
    if 'A' <= i <= 'Z':
        print(i.lower(), end="")
    elif 'a' <= i <= 'z':
        print(i.upper(), end="")
    else:
        print(i, end="")
print()

