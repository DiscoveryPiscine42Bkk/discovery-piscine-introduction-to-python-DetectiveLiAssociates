#!/usr/bin/env python3

arr_0 = [2, 8, 9, 48, 8, 22, -12, 2]
set_1 = set()

for i in arr_0:
    if i > 5:
        set_1.add( i + 2 )
    else:
        pass

print(f"Original array: {arr_0}")
print(f"New array: {set_1}")
