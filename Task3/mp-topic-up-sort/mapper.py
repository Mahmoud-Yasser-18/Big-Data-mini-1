#!/usr/bin/python3

import sys
import nltk
import json
from topic_list import extract_topic
for line in sys.stdin:
    if nltk.pos_tag([line.split("\t")[0].replace("__up__","").replace("__down__","")])[0][1] == "NN":
        print(line)


