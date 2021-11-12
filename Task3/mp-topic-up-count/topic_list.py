# extract topic from Body
import time 
import re
from forbidden import forbidden_words 

def extract_topic(body_text, subreddit,spaCy=False,debug=False):
    if body_text=="[deleted]":
        return []
    body_text=re.sub(r"""(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,;@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])""", ' ',body_text, flags=re.MULTILINE)
    body_text=re.sub(r"""\^""", ' ', body_text, flags=re.MULTILINE)
    body_text=re.sub(r"""\-""", ' ', body_text, flags=re.MULTILINE)
    body_text=re.sub(r"""\|""", ' ', body_text, flags=re.MULTILINE)
    body_text=re.sub(r"""\s\s+""", ' ', body_text, flags=re.MULTILINE)
    body_text=" "+body_text+" "
    
    body_text=re.sub(r"""[^\w]\.?\:?\;?\'?\"?\~?\@?\#?\$?\%?\^?\&?\*?\(?\)?""", ' ', body_text, flags=re.MULTILINE)
    body_text=re.sub(r"""\s[\w]\s""", ' ', body_text, flags=re.MULTILINE)
    print(body_text)

    resultwords  = [word for word in body_text.split(" ") if " "+word.lower()+" " not in forbidden_words and word.strip()!=""]
    print(resultwords)

    if not subreddit:
        return resultwords
    resultwords=[subreddit+"_sep_"+noun for noun in resultwords]

    return resultwords 
if __name__=="__main__":
    print("Using NLTK:")
    print(extract_topic("Very fast, thank you!","Asmerriddit"))
    print("="*20)
    print("Using spaCy:")
    print(extract_topic("It's due to all my family members off doing different things, and I don't feel like going to a bar.","Asmerriddit"))
    print(extract_topic("I had a dinner with my friends","Asmerriddit"))
