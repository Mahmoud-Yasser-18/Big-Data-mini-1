#!/usr/bin/python3
import os
import json
import sys
from topic_list import extract_topic

# Notes :
# 1. All Down votes are 0
# 2. All Controversiality are 0


# Option or NLP: NLTK, spaCy

f = open("./part-00000", "r")
top_subreddits=[line.split("\t")[1].replace("\n","") for line in f.readlines() if line != "\t\n"]


for line in sys.stdin:
    j_i=json.loads(line)
    if j_i["subreddit"] in top_subreddits:
        topics = extract_topic(j_i["body"],j_i["subreddit"],spaCy=True)
        for topic in topics:
            print(topic,1,sep="\t")

        




