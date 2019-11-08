#!/usr/bin/python3

# Resplit test and training data to get more training data.

import csv
import random
import sys

# Bipartition the data according to f.
def split(data, f):
    result = [[], []]
    for t in data:
        result[f(t)].append(t)
    return tuple(result)

# Read in a CSV file containing data.
def parse(filename):
    with open(filename, "r") as f:
        rows = csv.reader(f)
        data = []
        for row in rows:
            c = int(row[0])
            fs = [int(f) for f in row[1:]]
            data.append((c, fs))
        return data

# Generate a CSV file from the data.
def gen(filename, data):
    with open(filename, "w") as f:
        rows = csv.writer(f)
        for c, fs in data:
            rows.writerow([c] + fs)

# Do the resplits.
for cl in ["orig", "itg"]:
    train = parse("spect-" + cl + ".train.csv")
    test = parse("spect-" + cl + ".test.csv")
    data = train + test
    random.shuffle(data)
    pos, neg = split(data, lambda t: t[0])
    tpos = 2 * len(pos) // 3
    tneg = 2 * len(neg) // 3
    train = pos[:tpos] + neg[:tneg]
    test = pos[tpos:] + neg[tneg:]
    if cl == "orig":
        prefix = "spect-resplit"
    else:
        prefix = "spect-resplit-" + cl
    gen(prefix + ".train.csv", train)
    gen(prefix + ".test.csv", test)
