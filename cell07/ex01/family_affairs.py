#!/usr/bin/python3

def find_the_redheads(searchHair:dict)->list:   
    return list(filter(lambda name:searchHair[name]=="red",searchHair.keys()))

if __name__ == "__main__":

    dupont_family={
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }

    print(find_the_redheads(dupont_family))



