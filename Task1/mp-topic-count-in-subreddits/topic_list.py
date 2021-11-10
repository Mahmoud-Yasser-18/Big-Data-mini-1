# extract topic from Body
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
import time 
import re
from forbidden import forbidden_words 

stop_words = set(stopwords.words('english'))
nlp = spacy.load("en_core_web_sm")

 
def extract_topic(body_text, subreddit,spaCy=False,debug=False):
    if body_text=="[deleted]":
        return []
    body_text=re.sub(r"""(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,;@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])""", ' ', x, flags=re.MULTILINE)
    # body_text=re.sub(r"""(?:__|[*#])|\[(.*?)\]\(.*?\)""", ' ', body_text, flags=re.MULTILINE)
    body_text=re.sub(r"""\^""", ' ', body_text, flags=re.MULTILINE)
    body_text=re.sub(r"""\-""", ' ', body_text, flags=re.MULTILINE)
    body_text=re.sub(r"""\|""", ' ', body_text, flags=re.MULTILINE)
    body_text=re.sub(r"""\s\s+""", ' ', body_text, flags=re.MULTILINE)
    body_text=" "+body_text+" "
    if not spaCy:
        start = time.time()    
        word_tokens_body = word_tokenize(body_text)
        filtered_sentence = [w+"_"+subreddit for w in word_tokens_body if (not w.lower() in stop_words) and (w.lower() not in forbidden_words)]
        if debug:
            print("time taken for NLTK:")
            print(time.time()-start)
        return filtered_sentence
    
    start = time.time()    
    processed_body = nlp(body_text)
    nouns = [ " "+str(noun).lower()+" " for noun in processed_body.noun_chunks if " "+str(noun).lower()+" " not in forbidden_words]
    results=[]
    for n in range(len(nouns)):
        for word in forbidden_words:
            nouns[n]=nouns[n].replace(word," ")
        nouns[n]=nouns[n].strip()
        nouns[n]=re.sub(r"""\s\s+""", ' ', nouns[n], flags=re.MULTILINE)
        nouns[n]=nouns[n].strip()
        
        temp = nlp(nouns[n])
        if len(temp)>0:
            
            nouns[n]= " ".join([token.text for token in temp[:-1] if str(token.pos_) in ["NOUN","ADJ"] ]+[temp[-1].lemma_])
        
        if nouns[n] !="":
            results.append(nouns[n]+"_sep_"+subreddit)

    if debug:
        print("time taken for spaCy:")
        print(time.time()-start)
    return results 
if __name__=="__main__":
    print("Using NLTK:")
    print(extract_topic("Very fast, thank you!","Asmerriddit",debug=True))
    print("="*20)
    print("Using spaCy:")
    print(extract_topic("It's due to all my family members off doing different things, and I don't feel like going to a bar.","Asmerriddit",spaCy=True,debug=True))
    print(extract_topic("I had a dinner with my friends","Asmerriddit",spaCy=True,debug=True))
    doc =nlp("It's due to all my family members off doing massively different things")
    for token in doc:
        print("="*20)
        print(token, token.pos_,spacy.explain(token.pos_),spacy.explain(token.tag_),sep=", ")