#!/usr/bin/env python3

leaps_1 = []
for year in range(1900, 1940):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leaps_1.append(year)

leaps_2 = [y for y in range(1900, 1940)
           if (y % 4 == 0 and y % 100 !=0) or (y % 400 == 0)]

print(f"leap years between 1900 and 1940 by loop: {leaps_1},\n and by list comprehensions: {leaps_2}")
