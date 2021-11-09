import os
import json
import sys

# Notes :
# 1. All Down votes are 0
# 2. All Controversiality are 0


# Option or NLP: NLTK, spaCy


for line in sys.stdin:
    j_i=json.loads(line)
    if j_i["subreddit"] == '[deleted]':
        print(j_i["subreddit"],1,sep="\t")
    # print("j_i[ups]",j_i["ups"])
    # print("j_i[downs]",j_i["downs"])
    # print("j_i[score]",j_i["score"])
    # print(json.dumps(j_i, indent=4))



