#!/usr/bin/env python3

import sys
import unicodedata


def print_unicode_table(words):
    print(f"decimal   hex   chr  {'name':^40}")
    print("-------  -----  ---  " + f"{'':-<40}")

    code = ord(" ")
    end = min(0xD800, sys.maxunicode)  # Stop at surrogate pairs

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        match = True
        for word in words:
            if word is None or word not in name.lower():
                match = False
                break
        if match:
            print(f"{code:7d}  {code:5X}  {code:^3c}  {name.title()}")
        code += 1


words = []
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print(f"usage: {sys.argv[0]} [string1, string2, ...]")
        words = None
    else:
        for word in sys.argv[1:]:
            words.append(word.lower())
if words is not None:
    print_unicode_table(words)

