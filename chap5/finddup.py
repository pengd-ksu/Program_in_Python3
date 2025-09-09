#!/usr/bin/env python3

import collections
import os
import sys
from pathlib import Path

def find_duplicates(path):
    data = collections.defaultdict(list)

    for root, dirs, files in os.walk(path):
        for filename in files:
            fullname = Path(root) / filename
            key = (os.path.getsize(fullname), filename)
            data[key].append(fullname)

    for size, filename in sorted(data):
        names = data[(size, filename)]
        if len(names) > 1:
            print(f"{filename} ({size} bytes) may be duplicated "
                "({len(names)} files):")
            for name in names:
                print(f"\t{name}")

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    find_duplicates(path)

if __name__ == "__main__":
    main()