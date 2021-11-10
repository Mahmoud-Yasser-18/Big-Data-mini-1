#!/usr/bin/python3

import sys
import json

for line in sys.stdin:
    print(format(int(line.strip().split('\t')[1]), '032b').replace('0','b').replace('1','a'),line.strip().split('\t')[0],sep = "\t")
    
    


