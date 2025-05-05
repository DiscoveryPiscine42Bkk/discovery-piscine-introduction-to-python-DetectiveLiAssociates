#!/usr/bin/env python3

the_age = int(input("Please tell me your age: ").strip())

if the_age <= 0:
    pass
else:
    print(f"You are currently {the_age} years old")
    for i in range(1, 4):
        factor = 10
        the_age = the_age + 10
        print(f"In {i*factor} years, you'll be {the_age} years old")
        
