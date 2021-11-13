#!/usr/bin/python3

import sys
import nltk
import json


for line in sys.stdin:
    try :
        if nltk.pos_tag([line.split("\t")[0].split("_sep_")[1]])[0][1] == "NN":
            print(line)
    except:
        pass

