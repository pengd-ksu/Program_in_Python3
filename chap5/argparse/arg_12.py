#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2

""" 
bugfix: replace == with >=
From chatgpt:
1) Why >= fails but == doesn’t

The ordering operators (<, <=, >, >=) ask the objects to define a relative order via 
their rich comparison methods: __lt__, __le__, __gt__, __ge__.

In Python 3, if two objects don’t define a meaningful ordering with each other, you get TypeError
 (e.g., None >= 1).

It’s not limited strictly to “same type,” but to types that define cross-type ordering. Numbers 
like int and float do; many unrelated types don’t.

The equality operators (==, !=) call __eq__ / __ne__. If no special equality is defined, Python falls 
back to identity (are they the same object?). This just yields True/False; it doesn’t raise for 
unrelated types. Hence None == 1 → False.

Best practice: check for None with is None / is not None, not ==.

2) Correction: == does not compare __repr__

Equality in Python uses __eq__, not __repr__ (or string conversion). Two objects can print the same 
(__repr__ identical) yet still be unequal, and vice versa.

Quick demos:

# Equality does NOT use repr
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

How comparisons actually dispatch

a >= b tries a.__ge__(b). If that returns NotImplemented, it tries b.__le__(a). If still 
NotImplemented, it raises TypeError.

a == b tries a.__eq__(b). If NotImplemented, it tries b.__eq__(a). If both say NotImplemented, 
it falls back to identity equality (via object.__eq__).

Takeaways

>= implies an ordering relation, which only works when the operand types define one (not 
necessarily the same type, but compatible).

== checks semantic equality via __eq__, not __repr__.

For your argparse case, args.verbosity being None only breaks with ordering (e.g., >= 1), not 
with equality (== 1). Setting default=0 (or level = args.verbosity or 0) avoids the TypeError.
"""
if args.verbosity >= 2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity >= 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)