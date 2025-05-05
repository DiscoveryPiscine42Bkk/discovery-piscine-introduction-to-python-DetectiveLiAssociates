#!/usr/bin/env python3

the_number = int(input("Enter a number\n").strip())

for i in range(10):
    the_result = i * the_number
    print(f"{i} x {the_number} = {the_result}", end="\n")

