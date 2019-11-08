#!/usr/bin/python3

import csv
import math
import sys

m = 0.5

def split(data, f):
    result = [[], []]
    for t in data:
        result[f(t)].append(t)
    return tuple(result)

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

def pr(n, d):
    return math.log((n + m) / (d + m))

def itg(data):
    ndata = len(data)
    nfeatures = len(data[0][1])
    u0 = u(data)
    splits = []
    for i in range(nfeatures):
        data.sort(key=lambda t: t[1][i])
        sps = []
        for j in range(1, len(data)):
            us = u0 - ((j-1)/ndata) * u(data[:j]) - ((ndata-j+1)/ndata) * u(data[j:])
            sps.append((j, us))
        j, us = max(sps, key=lambda sp: sp[1])
        splits.append(data[j][1][i])
    return splits
            
def parse(filename):
    with open(filename, "r") as f:
        rows = csv.reader(f)
        data = []
        for row in rows:
            c = int(row[0])
            fs = [int(f) for f in row[1:]]
            data.append((c, fs))
        return data

def gen(filename, splits, data):
    with open(filename, "w") as f:
        rows = csv.writer(f)
        for c, fs in data:
            bfs = [int(fs[i] < splits[i]) for i in range(len(fs))]
            rows.writerow([c] + bfs)

train = parse("SPECTF.train")
test = parse("SPECTF.test")
splits = itg(train+test)
gen("spect-itg.train.csv", splits, train)
gen("spect-itg.test.csv", splits, test)
