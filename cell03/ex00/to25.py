#!/usr/bin/env python3

the_number = int(input("Enter a number less than 25:\n").strip())

if the_number > 25:
    print("Error")
else:
    while the_number <= 25:
        print(f"Inside the loop, my variable is {the_number}", end="\n")
        the_number += 1

