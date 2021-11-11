import string
from collections import Counter



def get_emotions(text_body) :
    lower_case = text_body.lower() 
    # converting to lowercase

    # Removing punctuations
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

    # splitting text into words
    tokenized_words = cleaned_text.split()

    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
                "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
                "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
                "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
                "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    # Removing stop words from the tokenized words list
    final_words = [word for word in tokenized_words if word not in stop_words]

    # Get emotions text
    emotion_list = []
    with open('./mp-emotion-count/emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
            word, emotion = clear_line.split(':')
            if word in final_words:
                emotion_list.append(emotion)

    w = Counter(emotion_list)
    return(w)

if __name__ == '__main__' :
    print (get_emotions("""I can't agree with passing the blame, but I'm
    glad to hear it's at least helping you with the anxiety. I
    went the other direction and started taking responsibility
    for everything. I had to realize that people make mistakes
    including myself and it's gonna be alright. I don't have to
    be shackled to my mistakes and I don't have to be afraid of
    making them"""))