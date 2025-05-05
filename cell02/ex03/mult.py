#!/usr/bin/env python3

the_first_number = int(input("Enter the first number:\n").strip())
the_second_number = int(input("Enter the first number:\n").strip())

mult_result = the_first_number * the_second_number

if mult_result < 0:
    is_signed = "The result is negative."
elif mult_result > 0:
    is_signed = "The result is positive."
else:
    is_signed = "The result is positive and negative."

print(f"{the_first_number} x {the_second_number} = {mult_result}", end="\n")
print(is_signed, end="\n")
