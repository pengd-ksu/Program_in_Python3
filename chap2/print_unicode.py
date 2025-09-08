#!/usr/bin/env python3

import sys
import unicodedata


def print_unicode_table(word):
    print(f"decimal   hex   chr  {'name':^40}")
    print("-------  -----  ---  " + f"{'':-<40}")

    code = ord(" ")
    end = min(0xD800, sys.maxunicode)  # Stop at surrogate pairs

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        if word is None or word in name.lower():
            print(f"{code:7d}  {code:5X}  {code:^3c}  {name.title()}")
        code += 1


word = None
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print(f"usage: {sys.argv[0]} [string]")
        word = 0
    else:
        word = sys.argv[1].lower()
if word != 0:
    print_unicode_table(word)

