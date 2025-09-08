#!/usr/bin/env python3
def get_int(msg):
    while True:
        try:
            i = int(input(msg))
            return i
        except ValueError as err:
            print(err)

if __name__ == "__main__":
    age = get_int("enter your age: ")
    print(f"Your age: {age}")


