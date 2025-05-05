#!/usr/bin/python3

import sys
import re

container = []

if(len(sys.argv)<2) or (len(sys.argv)>3):
    print("none")
else:
    for i in range(int(sys.argv[1]),(int(sys.argv[2])+1)):
        container.append(i)
    print(container)
