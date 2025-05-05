#!/usr/bin/python3

import sys

def downcase_all(the_text:str)->str:
    return the_text.lower();

if __name__ == "__main__":

    if len(sys.argv)<2:
        print("none")
    else:
        for i in sys.argv[1:]:
            print(downcase_all(i))
