#!/usr/bin/python3
import os
import json
import sys

from topic_list import extract_topic

# Notes :
# 1. All Down votes are 0
# 2. All Controversiality are 0


# Option or NLP: NLTK, spaCy

f = open("./mp-topic-count-in-subreddits/part-00000", "r")
#f = open("./part-00000", "r")
top_subreddits=[line.split("\t")[0].replace("\n","") for line in f.readlines() if line != "\t\n"]


for line in sys.stdin:
    try: 
        j_i=json.loads(line)
    except:
        continue
    if j_i["subreddit"] in top_subreddits:
        topics = extract_topic(j_i["body"],j_i["subreddit"],spaCy=True)
        for topic in topics:
            print(topic,1,sep="\t")

        




