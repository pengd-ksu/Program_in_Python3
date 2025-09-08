#!/usr/bin/env python3

def append_if_even_wrong(x, lst=[]):
    if x % 2 == 0:
        lst.append(x)
    return lst

def append_if_even_right(x, lst=None):
    lst = [] if lst is None else lst
    if x % 2 == 0:
        lst.append(x)
    return lst



def main():
    print(f"We do append_if_even_wrong(2): {append_if_even_wrong(2)}, and append_if_even_wrong(4): {append_if_even_wrong(4)}")
    print(f"We do append_if_even_right(2): {append_if_even_right(2)}, and append_if_even_right(4): {append_if_even_right(4)}")




if __name__ == "__main__":
    main()
