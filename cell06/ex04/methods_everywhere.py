#!/usr/bin/python3

import sys

def shrink(the_word:str):
    new_word = slice(0,8)
    print(the_word[new_word])

def enlarge(the_word:str):
    while len(the_word) < 8:
        the_word += 'Z'
    print(the_word)

if __name__ == "__main__":

    if len(sys.argv)<2:
        print("none")
    else:
        for i in sys.argv[1:]:
            if (len(i) > 8):
                shrink(i)
            else:
                enlarge(i)
