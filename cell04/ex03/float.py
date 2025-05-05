#!/usr/bin/env python3

the_given_number = float(input("Give me a number: ").strip())

int_process = int(the_given_number)

if int_process == the_given_number:
    print("This number is an integer")
else:
    print("This number is a decimal")

