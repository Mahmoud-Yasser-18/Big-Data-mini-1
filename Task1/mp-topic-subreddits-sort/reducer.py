#!/usr/bin/python3

import sys

word = None
count = 0

f = open("./mp-topic-subreddits-sort/part-00000", "r")
top_subreddits=[line.split("\t")[1].replace("\n","") for line in f.readlines() if line != "\t\n"]
top_subreddits_count={t:0 for t in top_subreddits} 

for line in sys.stdin:
    if line=="\t\n":
        continue
    if top_subreddits_count[line.split("\t")[1].split("_sep_")[0].replace("\n","")]>=10:
        continue
    print(line.replace("\n",""))
    top_subreddits_count[line.split("\t")[1].split("_sep_")[0].replace("\n","")]+=1