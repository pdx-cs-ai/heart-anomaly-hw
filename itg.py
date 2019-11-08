#!/usr/bin/python3

# Binarize scalar features via information-theoretic gain
# maximization.

import csv
import math
import sys

# M-estimator for probabilities.
m = 0.5

# Bipartition the data according to f.
def split(data, f):
    result = [[], []]
    for t in data:
        result[f(t)].append(t)
    return tuple(result)

# Compute the entropy of the data.
def u(data):
    ndata = len(data)
    cn, cp = split(data, lambda t: t[0])
    result = 0
    ncn = len(cn)
    if ncn > 0:
        pn = ncn / ndata
        result -= pn * math.log2(pn)
    ncp = len(cp)
    if ncp > 0:
        pp = ncp / ndata
        result -= pp * math.log2(pp)
    return result

# Log-probability with m-estimator.
def pr(n, d):
    return math.log((n + m) / (d + m))

# Find best split for each feature of the data.
def itg(data):
    ndata = len(data)
    nfeatures = len(data[0][1])
    # Entropy of whole dataset. Not necessary,
    # but pedagogical.
    u0 = u(data)
    # Splitpoint for each feature.
    splits = []
    for i in range(nfeatures):
        # Order the data by feature i value.
        data.sort(key=lambda t: t[1][i])
        # Try each possible splitpoint and
        # note the information gain.
        sps = []
        for j in range(1, len(data)):
            us = u0
            us -= (j/ndata) * u(data[:j])
            us -= ((ndata-j)/ndata) * u(data[j:])
            sps.append((j, us))
        # Save the best splitpoint.
        j, us = max(sps, key=lambda sp: sp[1])
        splits.append(data[j][1][i])
    return splits
            
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

# Generate a CSV file from the data. Do the splits here.
def gen(filename, splits, data):
    with open(filename, "w") as f:
        rows = csv.writer(f)
        for c, fs in data:
            bfs = [int(fs[i] < splits[i]) for i in range(len(fs))]
            rows.writerow([c] + bfs)

# Run all the things.
train = parse("SPECTF.train")
test = parse("SPECTF.test")
splits = itg(train+test)
gen("spect-itg.train.csv", splits, train)
gen("spect-itg.test.csv", splits, test)
