#!/usr/bin/python3

import sys

word = None
count = 0

for line in sys.stdin:
    print(line)
    count += 1
    if count == 20 :
        break