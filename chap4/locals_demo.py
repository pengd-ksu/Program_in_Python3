#!/usr/bin/env python3
global_var = "hello"

def demo(a, b):
    x = 42
    print(locals())

def main():
    demo(1, 2)

if __name__ == "__main__":
    main()
