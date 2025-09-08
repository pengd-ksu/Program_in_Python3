#!/usr/bin/env python3

nums = []
lowest = highest = None
total = 0

while True:
    try:
        line = input("enter a number or Enter to finish:")
        if not line:
            break
        num = int(line)
        nums.append(num)
        total += num
        if lowest is None or lowest > num:
            lowest = num
        if highest is None or highest < num:
            highest = num
    except ValueError as err:
        print(err)

s = sum(nums)
l = len(nums)
m = s / l
print(f"numbers: {nums}")
print(f"count = {l} sum = {s} lowest = {lowest} highest = {highest} mean = {m}") 
