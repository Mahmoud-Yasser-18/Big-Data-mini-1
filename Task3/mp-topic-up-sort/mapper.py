#!/usr/bin/python3

import sys
import json
from topic_list import extract_topic
for line in sys.stdin:
    if nltk.pos_tag([line.split(" ")[0]]) [1] == "NN":
        print(line)


