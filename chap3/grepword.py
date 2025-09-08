#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("usage: grepword.py word infile1 [infile2 [... infileN]]")
    sys.exit()

word = sys.argv[1]
for filename in sys.argv[2:]:
    with open(filename) as file:
        for lino, line in enumerate(file, start=1):
            if word in line:
                print(f"{filename}:{lino}:{line.rstrip():.40}")
