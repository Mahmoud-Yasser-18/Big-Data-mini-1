#!/usr/bin/python3

import sys

word = None
count = 0

from collections import defaultdict

f = open("./mp-author-topic-sort-subreddits/part-00000", "r")

top_topics_subreddits=[line.split("\t")[1].split("_sep_") for line in f.readlines() if line != "\t\n"]
global_dict = defaultdict(list)
for subreddit,topic in top_topics_subreddits:
    global_dict[subreddit.replace("\n","")].append(topic.replace("\n",""))
print(global_dict)
top_subreddits_topic_count={subr:{t:0 for t in global_dict[subr]} for subr in global_dict.keys()}
print(top_subreddits_topic_count)