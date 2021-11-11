#!/usr/bin/python3
import os
import json
import sys

from topic_list import extract_topic

# Notes :
# 1. All Down votes are 0
# 2. All Controversiality are 0


# Option or NLP: NLTK, spaCy

for line in sys.stdin:
    j_i=json.loads(line)
    topics = extract_topic(j_i["body"],None,spaCy=True)
    if j_i['ups']>0:
        for topic in topics:
            print("__up__"+topic,j_i['ups'],sep="\t")
    else :
        for topic in topics:
            print("__down__"+topic,j_i['ups'],sep="\t")

        




