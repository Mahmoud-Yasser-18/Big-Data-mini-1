#!/usr/bin/python3

import sys

word = None
count = 0

from collections import defaultdict


f = open("../mp-author-topic-count-in-subreddits/part-00000", "r")
#f = open("./part-00000", "r")

top_topics_subreddits=[line.split("\t")[0].split("_sep_") for line in f.readlines() if line != "\t\n"]
global_dict = defaultdict(list)
for topic,subreddit in top_topics_subreddits:
    global_dict[subreddit.replace("\n","")].append(topic.replace("\n",""))
top_subreddits_topic_count={subr:{t:[] for t in global_dict[subr]} for subr in global_dict.keys()}

for line in sys.stdin:
    try:
        key, value = line.strip().split(sep='\t')
        value=int(value)
    except:
        continue
    subr= key.split("_sep_")[1].replace("\n","")
    topic= key.split("_sep_")[2].replace("\n","")
    
    if len(top_subreddits_topic_count[subr][topic])>0:    
        if value>top_subreddits_topic_count[subr][topic][0][0] or len(top_subreddits_topic_count[subr][topic])<10:
            top_subreddits_topic_count[subr][topic].append((value,key))
            top_subreddits_topic_count[subr][topic]=sorted(top_subreddits_topic_count[subr][topic])[-10:]
            
    else:
        top_subreddits_topic_count[subr][topic].append((value,key))

for k,v in top_subreddits_topic_count.items():
    # print(v)
    for kr,vr in v.items():
        for r in vr :
            print(r[1],r[0],sep='\t')
