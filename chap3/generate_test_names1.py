#!/usr/bin/env python3

import random

def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames, "../data/forenames.txt"),
                            (surnames, "../data/surnames.txt")):
        with open(filename, encoding="utf8") as file:
            for name in file:
                names.append(name.rstrip())
    return forenames, surnames

forenames, surnames = get_forenames_and_surnames()
with open("test-names1.txt", "w", encoding="utf8") as file:
    for _ in range(100):
        line = f"{random.choice(forenames)} {random.choice(surnames)}\n"
        file.write(line)

