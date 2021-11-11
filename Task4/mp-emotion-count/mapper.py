#!/usr/bin/python3
import os
import json
import sys
from get_emotion import get_emotions
from topic_list import extract_topic

# Notes :
# 1. All Down votes are 0
# 2. All Controversiality are 0


# Option or NLP: NLTK, spaCy

top_subreddits_file = open ('part-00000','r')
top_subreddits = [line.split("\t")[1].replace("\n","") for line in top_subreddits_file.readlines() if line != "\t\n"]

for line in sys.stdin:
    j_i=json.loads(line)
    
    if j_i["subreddit"] in top_subreddits : 
        
        emotions = get_emotions(j_i["body"])
        for emotion,count in emotions.items():
            print(j_i["subreddit"]+"_sep_"+emotion,count,sep='\t')




