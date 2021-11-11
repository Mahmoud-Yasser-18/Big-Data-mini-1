#!/usr/bin/python3
import os
import json
import sys

# Notes :
# 1. All Down votes are 0
# 2. All Controversiality are 0


# Option or NLP: NLTK, spaCy

for line in sys.stdin:
    try: 
        j_i=json.loads(line)
    except:
        continue
    print(j_i['controversiality'],1,sep="\t")


