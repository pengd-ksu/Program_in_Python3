#!/usr/bin/env python3

import random, sys

articles = ["the", "a", "another", "her", "his"]
subjects = ["cat", "dog", "horse", "man", "woman", "boy", "girl"]
verbs = ["sang", "ran", "jumped", "said", "fought", "swam", "saw",
         "heard", "felt", "slept", "hopped", "hoped", "cried",
         "laughed", "walked"]
adverbs = ["loudly", "quietly", "quickly", "slowly", "well", "badly",
           "rudely", "politely"]

num = 5

if (len(sys.argv)) > 1:
    try:
        n = int(sys.argv[1])
        if 1 <= n <= 10:
            num = n
        else:
            print("lines must be between 1 and 10 inclusive")
    except ValueError:
        print("usage: awfulpoetry2_ans.py <number>")

for i in range(num):
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)

    if random.randint(0, 1):
        print(article, subject, verb, adverb)
    else:
        print(article, subject, verb)
