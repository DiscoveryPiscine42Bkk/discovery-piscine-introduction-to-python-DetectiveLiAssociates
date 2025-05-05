#!/usr/bin/python3

import sys
import re

if(len(sys.argv)!=2):
    print("none")
else:
    comparison = input("What was the parameter ? ")
    if re.findall(sys.argv[1],comparison):
        print("Good job!")
    else:
        print("Nope, sorry...")

