#!/usr/bin/python3

def average(valueScore:dict)->int:   
    sum = 0
    for i in valueScore:
        sum += valueScore[i]
    sum /= len(valueScore)
    return sum

if __name__ == "__main__":

    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
        }
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
        }

    print(f"Average for class 3B: {average(class_3B):,.2f}")

    print(f"Average for class 3C: {average(class_3C):,.2f}")



