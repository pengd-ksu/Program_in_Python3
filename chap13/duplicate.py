#!/usr/bin/env python3

import re

def duplicate(text):
    double_word_re = re.compile(r"\b(?P<word>\w+)\s+(?P=word)(?!\w)", re.IGNORECASE)

    for match in double_word_re.finditer(text):
        print("{0} is duplicated".format(match.group("word")))

if __name__ == "__main__":
    texts = ["win in vain", "one and and two let’s say, but but haha", "winer win"]
    for text in texts:
        duplicate(text)

