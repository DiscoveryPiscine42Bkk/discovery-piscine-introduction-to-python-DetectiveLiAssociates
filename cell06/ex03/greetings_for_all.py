#!/usr/bin/python3

def greetings_for_all(the_greet:str)->str:
    
    the_standard = "Hello, "
    
    if isinstance(the_greet, str):
        if the_greet == "":
            the_greetings = the_standard + "noble stranger."
        else:
            the_greetings = the_standard + the_greet + "."
        print(the_greetings)    
    else:
        the_greetings = "Error! It was not a name."
        print(the_greetings)

if __name__ == "__main__":

    try:
        people = ["Alexandria","Wil","",42]
        for i in people:
            greetings_for_all(i)
    except Exception as e:
        print(f"Exception Caught: {e}")
