#!/usr/bin/env python3
import sys

def equal_float(a, b):
    return abs(a - b) <= sys.float_info.epsilon

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 equal_float.py <num1> <num2>")
        sys.exit(1)

    print(f"sys.float_info.epsilon: {sys.float_info.epsilon}")

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
    except ValueError:
        print("Both arguments must be numbers.")
        sys.exit(1)

    if equal_float(a, b):
        print(f"{a} and {b} are equal!")
    else:
        print(f"{a} and {b} are not equal!")
