#!/usr/bin/env python3

import pickle

data = {"a": 1, "b": [1, 2, 3]}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

with open("data.pkl", "rb") as f:
    restored = pickle.load(f)

assert restored == data, f"restored: {restored} is not the same as data: {data}"
