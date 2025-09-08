#!/usr/bin/env python3

import random

articles = ["the", "a", "another", "her", "his"]
subjects = ["cat", "dog", "horse", "man", "woman", "boy", "girl"]
verbs = ["sang", "ran", "jumped", "said", "fought", "swam", "saw",
         "heard", "felt", "slept", "hopped", "hoped", "cried",
         "laughed", "walked"]
adverbs = ["loudly", "quietly", "quickly", "slowly", "well", "badly",
           "rudely", "politely"]

num = 5

for i in range(num):
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)

    if random.randint(0, 1):
        print(article, subject, verb, adverb)
    else:
        print(article, subject, verb)
