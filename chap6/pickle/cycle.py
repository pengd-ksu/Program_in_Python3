#!/usr/bin/env python3

import pickle

d = {}
d["self"] = d
blob = pickle.dumps(d)
out = pickle.loads(blob)

assert out is out["self"], "cycle is not preserved"

assert out is d, "the object is changed"
