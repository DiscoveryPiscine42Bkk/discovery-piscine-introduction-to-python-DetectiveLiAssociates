#!/usr/bin/python3

def famous_births(valToSort:dict):   
    the_scientists = sorted(valToSort.values(), key=lambda name:name['date_of_birth'])
    for eachPerson in the_scientists:
        print(f"{eachPerson['name']} is a great scientist botn in {eachPerson['date_of_birth']}")
    
if __name__ == "__main__":

    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }

    famous_births(women_scientists)

