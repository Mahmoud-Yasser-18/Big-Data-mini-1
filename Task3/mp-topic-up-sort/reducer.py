#!/usr/bin/python3

import sys

word = None
count_up = 0
count_down = 0

for line in sys.stdin:
    if line.split("\t")[1][:3]=="__u" and count_up<=10:
        print(line)
        count_up += 1
    if line.split("\t")[1][:3]=="__d" and count_down<=10:
        print(line)
        count_down += 1
    if count_down == 10 and  count_up == 10:
        break