# extract topic from Body
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import spacy
import time 
import re
from forbidden import forbidden_words as forbidden

stop_words = set(stopwords.words('english'))
nlp = spacy.load("en_core_web_sm")

 
def extract_topic(body_text, subreddit,spaCy=False,debug=False):
    body_text=re.sub(r"""(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])""", ' ', body_text, flags=re.MULTILINE)
    # body_text=re.sub(r"""(?:__|[*#])|\[(.*?)\]\(.*?\)""", ' ', body_text, flags=re.MULTILINE)
    body_text=re.sub(r"""\^""", '', body_text, flags=re.MULTILINE)
    body_text=re.sub(r"""\-""", '', body_text, flags=re.MULTILINE)
    body_text=re.sub(r"""\|""", '', body_text, flags=re.MULTILINE)
    body_text=re.sub(r"""\s\s+""", ' ', body_text, flags=re.MULTILINE)

    if not spaCy:
        start = time.time()    
        word_tokens_body = word_tokenize(body_text)
        filtered_sentence = [w+"_"+subreddit for w in word_tokens_body if (not w.lower() in stop_words) and (w.lower() not in forbidden)]
        if debug:
            print("time taken for NLTK:")
            print(time.time()-start)
        return filtered_sentence
    
    start = time.time()    
    processed_body = nlp(body_text)
    nouns = [ str(noun).lower()+"_sep_"+subreddit for noun in processed_body.noun_chunks if str(noun).lower() not in forbidden]
    if debug:
        print("time taken for spaCy:")
        print(time.time()-start)
    return nouns 
if __name__=="__main__":
    print("Using NLTK:")
    print(extract_topic("Very fast, thank you!","Asmerriddit",debug=True))
    print("="*20)
    print("Using spaCy:")
    print(extract_topic("Very fast, thank you!","Asmerriddit",spaCy=True,debug=True))