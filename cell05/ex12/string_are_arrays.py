#!/usr/bin/python3

import sys
import re

target = "z"

if(len(sys.argv)!=2):
    print("none")
else:
    the_z = re.findall(target,sys.argv[1])
    if len(the_z) == 0:
        print("none")
    else:
        for i in the_z:
            print("z",end="")
        print()
