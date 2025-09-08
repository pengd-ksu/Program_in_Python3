#!/usr/bin/env python3


margin = False
width = 100 + (10 if margin else 0)
print(f"width: {width}")


count = 0
print(f"{count if count != 0 else 'no'} file{'s' if count != 1 else ''}")


n = 3
while n > 0:
    print(f"n is now {n}")
    n -= 1
else:
    print(f"n is now {n} and the while loop ended normally")

n = 3
while n > 0:
    print(f"n is now {n}")
    if n == 2:
        break
    n -= 1
else:
    print(f"n is now {n} and the while loop ended normally")


# list doesn't have a corresponding str.find() that returns a -1
def list_find_while(lst, target):
    index = 0
    while index < len(lst):
        if lst[index] == target:
            break
        index += 1
    else:
        index = -1
    return index

print(f'list_find_while: {list_find_while("what are you doing?", "d")}')

def list_find_for(lst, target):
    for index, x in enumerate(lst):
        if x == target:
            break
    else:
        index = -1
    return index

print(f'list_find_for: {list_find_for("what are you doing?", "d")}')


# check how else and finally work in try except block
def try_else():
    try:
        x = int("123")
    except ValueError:
        print("conversion failed")
    else:
        print("conversion succeeded")
    finally:
        print("always runs")
try_else()

def try_except():
    try:
        x = int("abc")
    except ValueError:
        print("conversion failed")
    else:
        print("conversion succeeded")
    finally:
        print("always runs")
try_except()
