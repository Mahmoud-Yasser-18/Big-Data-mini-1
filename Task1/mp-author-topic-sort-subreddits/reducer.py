#!/usr/bin/python3

import sys

word = None
count = 0

from collections import defaultdict

# f = open("./mp-author-topic-count-in-subreddits/part-00000", "r")
f = open("./part-00000", "r")
top_topics_subreddits=[line.split("\t")[1].split("_sep_") for line in f.readlines() if line != "\t\n"]
global_dict = defaultdict(list)
for topic, subreddit in top_topics_subreddits:
    global_dict[subreddit.replace("\n","")].append(topic)

top_subreddits_topic_count={subr:{t:0 for t in global_dict[subr]} for subr in global_dict.keys()}
for line in sys.stdin:
    if line=="\t\n":
        continue
    if top_subreddits_topic_count[line.split("\t")[1].split("_sep_")[1].replace("\n","")][line.split("\t")[1].split("_sep_")[2].replace("\n","")]>=10:
        continue
    if sum(sum(topic.values()) for topic in [top_subreddits_topic_count.values()])==1000:
        break
    print(line.replace("\n",""))
    top_subreddits_topic_count[line.split("\t")[1].split("_sep_")[1].replace("\n","")][line.split("\t")[1].split("_sep_")[2].replace("\n","")]+=1