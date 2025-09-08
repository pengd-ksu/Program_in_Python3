#!/usr/bin/env python3

def print_args(*args, **kwargs):
    for i, arg in enumerate(args):
        print(f"positional argument {i} = {arg}")
    for key in kwargs:
        print(f"keyword argument {key} = {kwargs[key]}")

def main():
    args = (1, 3, 5, 7, 11, 13)
    dic = {"first" : 1, "second": 2, "third": 3}
    print(f"args is {args}, and dic is: {dic}")
    print_args(args, dic)

if __name__ == "__main__":
    main()
