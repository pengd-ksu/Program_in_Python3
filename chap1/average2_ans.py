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

swap = True
end = len(nums) - 1
while swap:
    if (end < 1):
        swap = False
    else:
        for i in range(end):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        end -= 1

s = sum(nums)
l = len(nums)
m = s / l
if l % 2 == 0:
    median = (nums[l // 2 - 1] + nums[l // 2]) / 2
else:
    median = nums[l // 2]
print(f"numbers: {nums}")
print(f"count = {l} sum = {s} lowest = {lowest} highest = {highest} mean = {m} median = {median}") 
