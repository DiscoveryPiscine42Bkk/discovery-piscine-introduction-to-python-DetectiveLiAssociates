#!/usr/bin/python3

def array_of_names(sortingData:dict):
    new_sorted_output = []
    for i in sortingData:
        new_sorted_output.append(i.capitalize()+" "+sortingData[i].capitalize())
    return new_sorted_output

if __name__ == "__main__":

    the_people={
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }

    print(array_of_names(the_people))
