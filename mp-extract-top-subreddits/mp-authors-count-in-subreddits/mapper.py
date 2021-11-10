#!/usr/bin/python3
import os
import json
import sys

# Notes :
# 1. All Down votes are 0
# 2. All Controversiality are 0


# Option or NLP: NLTK, spaCy

f = open("./top_subreddits.txt", "r")
top_subreddits=[line.split("\t")[1].replace("\n","") for line in f.readlines() if line != "\t\n"]


for line in sys.stdin:
    j_i=json.loads(line)
    if j_i["subreddit"] in top_subreddits:
        print(j_i["author"]+"_sep_"+j_i["subreddit"],1,sep="\t")