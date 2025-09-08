#!/usr/bin/env python3

import string, sys, collections

words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] = words.get(word, 0) + 1
# Use mobi dick in data folder as example                
limit = 20
line = 0
for word in sorted(words, key=lambda x: words[x], reverse=True):
    print(f"'{word}' occurs {words[word]} times")
    line += 1
    if line >= limit:
        break