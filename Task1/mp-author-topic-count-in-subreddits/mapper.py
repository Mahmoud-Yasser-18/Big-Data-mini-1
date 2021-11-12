#!/usr/bin/python3
import os
import json
import sys

# Notes :
# 1. All Down votes are 0
# 2. All Controversiality are 0

# Option or NLP: NLTK, spaCy
from collections import defaultdict

# f = open("./mp-author-topic-count-in-subreddits/part-00000", "r")
f = open("./part-00000", "r")
top_topics_subreddits=[line.split("\t")[0].split("_sep_") for line in f.readlines() if line != "\t\n"]
global_dict = defaultdict(list)
for topic,subreddit  in top_topics_subreddits:
    global_dict[subreddit.replace("\n","")].append(topic.replace("\n",""))
for line in sys.stdin:
    try: 
        j_i=json.loads(line)
    except:
        continue
    if j_i["subreddit"] in global_dict.keys():
        for topic in global_dict[j_i["subreddit"]]:
            if topic.lower() in j_i["body"].lower(): 
                print(j_i["author"] +"_sep_"+j_i["subreddit"]+"_sep_"+topic,1,sep="\t")