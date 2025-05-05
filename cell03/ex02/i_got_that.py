#!/usr/bin/env python3

prompt = input("What you gotta say? : ").strip()

break_phrase = "STOP"

while prompt != break_phrase:
    prompt = input("I got that! Anything else? : ").strip()

