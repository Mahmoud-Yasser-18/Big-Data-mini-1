#!/usr/bin/python3

import sys
import json

for line in sys.stdin:
    if line.split("\t")[0].split("_sep_")[0].replace("\n","")=="[deleted]":
        continue
    print(format(abs(int(line.strip().split('\t')[1])), '032b').replace('0','b').replace('1','a'),line.strip().split('\t')[0],sep = "\t")
    
    


