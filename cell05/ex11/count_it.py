#!/usr/bin/python3

import sys
import re

if(len(sys.argv)<2):
    print("none")
else:    
    print("parameters: ",len(sys.argv)-1)
    for i in sys.argv[1:]:
        print(str(i) + ": " + str(len(i)))
