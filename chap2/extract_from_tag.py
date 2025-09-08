#!/usr/bin/env python3

def extract_from_tag_index(tag, line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    try:
        i = line.index(opener)
        start = i + len(opener)
        j = line.index(closer, start)
        return line[start:j]
    except ValueError:
        return None

def extract_from_tag_find(tag, line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    i = line.find(opener)
    if i != -1:
        start = i + len(opener)
        j = line.find(closer, start)
        if j != -1:
            return line[start:j]
    return None

if __name__ == "__main__":
    print(extract_from_tag_find("red", "what a <red>rose</red> this is")) 
    print(extract_from_tag_index("red", "what a <red>rose</red> this is"))
