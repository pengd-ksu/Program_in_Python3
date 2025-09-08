#!/usr/bin/env python3
"""
$ ./global_var.py 
Traceback (most recent call last):
  File "/home/pengd/Documents/AI/AI_Tools/Program_in_Python3/chap4/./global_var.py", line 15, in <module>
    main()
  File "/home/pengd/Documents/AI/AI_Tools/Program_in_Python3/chap4/./global_var.py", line 11, in main
    set_language()
  File "/home/pengd/Documents/AI/AI_Tools/Program_in_Python3/chap4/./global_var.py", line 6, in set_language
    print(Language)
          ^^^^^^^^
UnboundLocalError: cannot access local variable 'Language' where it is not associated with a value
"""

Language = "en"

def set_language():
    print(Language)
    Language = "fr" # Create a local var


def main():
    set_language()
    print(f"Global Language is still: {Language}")

if __name__ == "__main__":
    main()

