#!/usr/bin/env python3

the_password="Python is awesome"

enter_pass = input().strip()

if enter_pass == the_password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
