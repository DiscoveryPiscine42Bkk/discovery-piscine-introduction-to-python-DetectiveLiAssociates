#!/usr/bin/env python3

the_first_number = float(input("Give me the first number: ").strip())
the_second_number = float(input("Give me the second number: ").strip())

print("Thank you!")

the_add = the_first_number + the_second_number
the_sub = the_first_number - the_second_number
the_mul = the_first_number * the_second_number

print(f"{the_first_number:.0f} + {the_second_number:.0f} = {the_add:.0f}")
print(f"{the_first_number:.0f} - {the_second_number:.0f} = {the_sub:.0f}")

if the_second_number == 0:
    the_div = "Non-Divisible by Zero"
    print(f"{the_first_number:.0f} / {the_second_number:.0f} = {the_div}")
else:
    the_div = the_first_number / the_second_number
    print(f"{the_first_number:.0f} / {the_second_number:.0f} = {the_div:.0f}")

print(f"{the_first_number:.0f} * {the_second_number:.0f} = {the_mul:.0f}")
