#!/usr/bin/python3

import sys

word = None
count = 0

for line in sys.stdin:
    try:
        key, value = line.strip().split(sep='\t')
    except:
        continue
    if word is None:
        word = key
    elif word != key:
        print(word, count, sep='\t')
        word = key
        count = 0
    count += int(value)
print(word, count, sep='\t')
