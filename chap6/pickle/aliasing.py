#!/usr/bin/env python3

import pickle

shared = {"k": 42}
obj = [shared, shared]
blob = pickle.dumps(obj)
out = pickle.loads(blob)

assert out[0] is out[1], "the object is changed"
