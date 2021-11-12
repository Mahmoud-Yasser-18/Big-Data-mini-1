#!/usr/bin/python3

import sys

word = None
count = 0

f = open("./mp-author-sort-subreddits/part-00000", "r")
#f = open("./part-00000", "r")
top_subreddits=[line.split("\t")[0].replace("\n","") for line in f.readlines() if line != "\t\n"]
top_subreddits_key_value={t:[] for t in top_subreddits} 

for line in sys.stdin:
    try:
        key, value = line.strip().split(sep='\t')
        value=int(value)
    except:
        continue
    try:
        subr= line.split("\t")[0].split("_sep_")[0].replace("\n","")
        if value>top_subreddits_key_value[subr][0][0] or len(top_subreddits_key_value)<10:
            top_subreddits_key_value[subr].append((value,key))
            top_subreddits_key_value[subr]=sorted(top_subreddits_key_value[subr])[-10:]
            
    except:
        try:
            subr= line.split("\t")[0].split("_sep_")[0].replace("\n","")
            top_subreddits_key_value[subr].append((value,key))
        except:
            pass

for k,v in top_subreddits_key_value.items():
    #v=[valus,key]
    for record in v:
        print(record[1],record[0],sep='\t')
