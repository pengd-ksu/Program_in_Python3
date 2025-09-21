#!/usr/bin/env python3

class Hashexample:
    def __eq__(self, other):
        return True

obj = Hashexample()
print(obj.__hash__)
print(hash(obj))

