#!/usr/bin/python3
import os
import json
import sys

# Notes :
# 1. All Down votes are 0
# 2. All Controversiality are 0

# Option or NLP: NLTK, spaCy
from collections import defaultdict

f = open("./mp-author-topic-count-in-subreddits/part-00000", "r")
#f = open("./part-00000", "r")
top_topics_subreddits=[line.split("\t")[1].split("_sep_") for line in f.readlines() if line != "\t\n"]
global_dict = defaultdict(list)
for subreddit,topic in top_topics_subreddits:
    global_dict[subreddit.replace("\n","")].append(topic.replace("\n",""))
print(global_dict)