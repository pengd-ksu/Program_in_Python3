#!/usr/bin/env python3

class A:
    def __repr__(self):
        return "A()"  # same repr for all instances

a, b = A(), A()
print(repr(a), repr(b))   # A() A()
print(a == b)             # False (default equality = identity)

# Custom equality uses __eq__, not repr
class B:
    def __init__(self, val): self.val = val
    def __repr__(self): return f"B({self.val})"
    def __eq__(self, other):
        if isinstance(other, B):
            return self.val == other.val
        return NotImplemented

print(B(1) == B(1))  # True (same val)
print(B(1) == B(2))  # False

# Ordering requires defined relational methods
try:
    print(None >= 1)   # raises TypeError
except TypeError as e:
    print("TypeError:", e)

print(None == 1)      # False (just equality, no error)
