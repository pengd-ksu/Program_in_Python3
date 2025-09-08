#!/usr/bin/env python3

def load_items(filename):
    fh = None
    print("1. Starting function")
    items = []
    try:
        print("2. Opening file")
        fh = open(filename, "r")
        print("3. Reading lines")
        items = fh.readlines()
        print("4. Success - no exception")
    except EnvironmentError as err:
        print("5. Exception occurred")
        return []
    finally:
        print("6. Finally block - always runs")
        if fh is not None:
            fh.close()
    print("7. About to return")
    return items

def main():
    load_items("test.txt")
    exit()

if __name__ == "__main__":
    main()
